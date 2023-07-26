from datasets.git import GitRepository


def main():
    repo = GitRepository.clone("https://github.com/pioneer01010/Funcherry.git",
                               "C:\\/Users\\/yc_pine.hong\\/Downloads\\/Funcherry")
    for rev in repo.rev_list():
        repo.checkout(rev)

if __name__ == '__main__':
    main()