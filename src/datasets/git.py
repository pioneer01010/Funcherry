import os
import logging
import subprocess
import shutil

from common.error import RepositoryError

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.DEBUG)

class GitRepository:
    def __init__(self, uri, path):

        if not os.path.exists(path):
            cause = "Git repository '%s' does not exist", uri
            raise RepositoryError(cause=cause)

        self.uri = uri
        self.path = path
        self.revision = "HEAD"

    @classmethod
    def clone(cls, uri, path, ssl_verify=True):
        cmd = ['git', 'clone', uri, path]

        if not ssl_verify:
            cmd += ['-c', 'http.sslVerify=false']
        if os.path.exists(os.path.join(path, '.git')):
            logger.warning("%s repository already exists in %s", uri, path)
            return cls(uri, path)

        cls._exec(cmd)
        logger.debug("Git %s repository cloned into %s", uri, path)

        return cls(uri, path)

    def rev_list(self, branches=None):
        cmd = ['git', 'rev-list', '--reverse']

        if branches is None:
            cmd.extend(['--branches', '--tags', '--remotes=origin'])
        elif len(branches) == 0:
            cmd.extend(['--branches', '--tags', '--max-count=0'])
        else:
            branches = ['refs/heads/' + branch for branch in branches]
            cmd.extend(branches)

        outs = self._exec(cmd, self.path)
        revs = outs.decode("utf-8").split('\n')

        return revs[:-1]

    def checkout(self, rev):
        cmd = ['git', 'checkout', rev]
        self._exec(cmd, self.path)
        self.revision = rev

        return rev

    @staticmethod
    def _exec(cmd, cwd=None):
        logger.debug("%s > %s", cwd, cmd)

        try:
            proc = subprocess.Popen(cmd,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    cwd=cwd)
            (outs, errs) = proc.communicate()
        except OSError as e:
            raise RepositoryError(cause=str(e))

        if proc.returncode != 0:
            logger.error("returncode=%d, errs=%s", proc.returncode, errs)

        return outs




