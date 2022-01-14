from imports import *

print('''\n

   ____ _ _   _           _       _____           _ 
  / ___(_) |_| |__  _   _| |__   |_   _|__   ___ | |
 | |  _| | __| '_ \| | | | '_ \    | |/ _ \ / _ \| |
 | |_| | | |_| | | | |_| | |_) |   | | (_) | (_) | |
  \____|_|\__|_| |_|\__,_|_.__/    |_|\___/ \___/|_|
                                                    
\n''')
username=input("Enter Github Username >> ")
repository=Repository(username)
issues=Issues(username)

print("\n[-] You can visit {} for more information about the user...".format(repository.userurl))

time.sleep(2)
try:
    # Creating the Main Menu
    with open("./files/mainmenu.txt","r") as f:
        print(f.read())
        f.close()

    repo_list=["[{}] {}".format(i[0]+1,i[1]) for i in enumerate(repository.listAllRepos().keys())]

    for i in repo_list:
        print(i)

    selected_repo_number=int(input("Enter Repository Number to select the Repository >> "))

    for repo in repo_list:
        if str(selected_repo_number) in repo:
            selected_reponame = repo.split(" ")[-1]


except KeyboardInterrupt:
    print("\nLeaving Github Tool...")
    sys.exit(0)


while True:
    try:
        with open("./files/helptext.txt",'r') as f:
            print(f.read())
            f.close()

        repo_option = int(input("Enter Option Number >> "))

        if repo_option==1:
            
            with open("./files/repooperations.txt","r") as f:
                print(f.read())
                f.close()

            repo_fuction_option=int(input("Enter Option Number to Perform the Operation on {} Repository >> ".format(selected_reponame)))

            if repo_fuction_option==1:
                repository.downloadRepo(selected_reponame)

            elif repo_fuction_option==2:
                repository.downloadAndExtractRepo(selected_reponame)
            
            elif repo_fuction_option==3:
                repository.displayLicense(selected_reponame)

                
        # Option-2: See Issues
        elif repo_option==2:
            issuesitem=issues.listIssues(selected_reponame)
            list_of_issues=["[{}] {}".format(i[0]+1,i[1]) for i in enumerate(issuesitem.keys())]
            
            if len(list_of_issues)==0:
                print("\nNo Issues in This Repository\n")

            else:
                for i in list_of_issues:
                    print(i)

                issue_number=int(input("Enter Issue Number to Read aboy the Issue >> "))

                for issue in list_of_issues:
                    if str(issue_number) in issue:
                        selected_issue=issue.split("] ")[-1]

                issues.readIssue(selected_issue)        
        
        # Option-3: Select Different Repository
        elif repo_option==3:

            repo_list=["[{}] {}".format(i[0]+1,i[1]) for i in enumerate(repository.listAllRepos().keys())]
            for i in repo_list:
                print(i)

            selected_repo_number=int(input("Enter Repository Number to select the Repository >> "))

            for repo in repo_list:
                if str(selected_repo_number) in repo:
                    selected_reponame = repo.split(" ")[-1]
        
        
        # If Wrong Option is selected
        else:
            print("<< Wrong Option ! Choose Between 1 - 3 >>")
                                    

    except KeyboardInterrupt:
        print("\nLeaving Github Tool...")
        break
