import logging

from datasets.git import GitRepository
from datasets.parser import FunctionParser
from common.log import GlobalLogger

GlobalLogger.initialize(log_level=logging.DEBUG)

def main():
    path = "C:\\/Users\\/yc_pine.hong\\/Downloads\\/Funcherry"
    repo = GitRepository.clone("https://github.com/pioneer01010/Funcherry.git", path)

    for rev in repo.rev_list():
        repo.checkout(rev)

    from pathlib import Path
    files = [f for f in Path(path).rglob('*.py') if not f.name.startswith("__init__")]
    for file in files:
        functions = FunctionParser.parse_functions_from_file(file)





if __name__ == '__main__':
    main()
