import json

from utils.gitc import GitClient


class TestGitClient:

    def test_clone(self, config_path):
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
            path = config['work_dir']
            for repo in config['sample_repo']['python']:
                result = GitClient.clone(repo, path)
                assert type(result) is GitClient

    def test_rev_list_and_checkout(self, config_path):
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
            path = config['work_dir']
            repo = config['sample_repo']['python'][0]
            client = GitClient.clone(repo, path)
            assert len(client.rev_list()) > 0

            for rev in client.rev_list(reverse=True):
                client.checkout(rev)