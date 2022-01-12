from imports import *

print('''\n

   ____ _ _   _           _       _____           _ 
  / ___(_) |_| |__  _   _| |__   |_   _|__   ___ | |
 | |  _| | __| '_ \| | | | '_ \    | |/ _ \ / _ \| |
 | |_| | | |_| | | | |_| | |_) |   | | (_) | (_) | |
  \____|_|\__|_| |_|\__,_|_.__/    |_|\___/ \___/|_|
                                                    

                                                                              
\n''')

username = input("Enter Github Username >> ")

repository = Repository(username)

while True:
    with open("helptext.txt", 'r') as f:
        print(f.read())
        f.close()

    option = int(input("Enter Option Number >> "))

    if option == 1:

        with open("repooperations.txt", "r") as f:
            print(f.read())
            f.close()

        repo_option = int(input("Enter Option Number >> "))

        if repo_option == 1:

            print("\nThe Repositories Present in {} is as follows :".format(username))

            for repo in enumerate(repository.listAllRepos().keys()):
                print("[{}] {}".format(repo[0]+1, repo[1]))

        elif repo_option == 2:

            repo_list = ["[{}] {}".format(x[0]+1, x[1])
                        for x in enumerate(repository.listAllRepos().keys())]

            print("\nSelect Repository You want to Download...")
            for repo in repo_list:
                print(repo)
            repo_number = int(input("Enter Repository Number >> "))

            for repo in repo_list:
                if str(repo_number) in repo:
                    reponame = repo.split(" ")[-1]

            repository.downloadRepo(reponame)

        elif repo_option == 3:

            for repo in repository.listAllRepos().keys():
                repository.downloadRepo(repo)

        elif repo_option == 4:
            repo_list = ["[{}] {}".format(x[0]+1, x[1])
                        for x in enumerate(repository.listAllRepos().keys())]

            print("\nSelect Repository You want to Download and Extract...")
            for repo in repo_list:
                print(repo)
            repo_number = int(input("Enter Repository Number >> "))

            for repo in repo_list:
                if str(repo_number) in repo:
                    reponame = repo.split(" ")[-1]

            repository.downloadAndExtractRepo(reponame)

        elif repo_option == 5:
            for repo in repository.listAllRepos().keys():
                repository.downloadAndExtractRepo(repo)
                