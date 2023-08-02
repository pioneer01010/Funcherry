import os
import logging

from git import Repo


class GitClient:
    def __init__(self, repo):
        self.client = repo.git

    @classmethod
    def clone(cls, uri, path):
        if os.path.exists(os.path.join(path, '.git')):
            logging.warning("%s repository already exists in %s", uri, path)
            return cls(Repo(os.path.join(path)))

        return cls(Repo.clone_from(uri, os.path.join(path)))

    def rev_list(self, branches=None, reverse=False):
        cmd = []
        if reverse:
            cmd.extend(['--reverse'])
        if branches is None:
            cmd.extend(['--branches', '--tags', '--remotes=origin'])
        elif len(branches) == 0:
            cmd.extend(['--branches', '--tags', '--max-count=0'])
        else:
            branches = ['refs/heads/' + branch for branch in branches]
            cmd.extend(branches)

        return self.client.rev_list(cmd).split('\n')

    def checkout(self, revision):
        cmd = [revision]
        self.client.checkout(cmd)
