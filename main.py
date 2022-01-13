from imports import *


username=input("Enter Github Username >> ")
repository=Repository(username)


# Creating the Main Menu
with open("mainmenu.txt","r") as f:
    print(f.read())
    f.close()
repo_list=["[{}] {}".format(i[0]+1,i[1]) for i in enumerate(repository.listAllRepos().keys())]
for i in repo_list:
    print(i)
selected_repo_number=int(input("Enter Repository Number to select the Repository >> "))

for repo in repo_list:
    if str(selected_repo_number) in repo:
        selected_reponame = repo.split(" ")[-1]

while True:
    try:
        with open("helptext.txt",'r') as f:
            print(f.read())
            f.close()

        repo_option = int(input("Enter Option Number >> "))

        if repo_option==1:
            
            with open("repooperations.txt","r") as f:
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
            print("You Have Come Into the Issues Section")

        
        
        # Option-3: See Pull Requests
        elif repo_option==3:
            print("You are in Pull Request")

        
        # Option-4: Select Different Repository
        elif repo_option==4:
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
