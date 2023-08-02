import logging

from utils.git import GitClient
from datasets.parser import FunctionParser
from common.log import GlobalLogger
from pathlib import Path

GlobalLogger.initialize(log_level=logging.DEBUG)


def main():
    repo = "https://github.com/pioneer01010/Funcherry.git"
    path = "C:\\/Users\\/yc_pine.hong\\/Downloads\\/Funcherry"

    client = GitClient.clone(repo, path)
    for rev in client.rev_list(reverse=True):
        client.checkout(rev)

        files = [f for f in Path(path).rglob('*.py') if not f.name.startswith("__init__")]
        for file in files:
            functions = FunctionParser.parse_functions_from_file(file)
            for func in functions:
                logging.info(func)


if __name__ == '__main__':
    main()
