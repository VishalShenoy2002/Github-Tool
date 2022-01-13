from imports import *    

class Repository:

    def __init__(self,username):

        self.username=username

        self.userurl="https://github.com/{}/".format(self.username)
        self.repourl="https://github.com/{}?tab=repositories".format(self.username)

        self.download_link="archive/refs/heads/main.zip"

        self.request=requests.get(self.repourl,allow_redirects=True)

        self.soup=BeautifulSoup(self.request.content,'html.parser')

        self.repositories={}


    def listAllRepos(self):
        
        for repo in self.soup.find_all("h3",class_="wb-break-all"):
            reponame=repo.a.text.strip()
            repolink=repo.a['href']
            self.repositories[reponame]=repolink

        return self.repositories

    def downloadRepo(self,repository_name):

        print("\n[*] Downloading {} Repository...".format(repository_name))
        self.current_repourl="{}{}/{}".format(self.userurl,repository_name,self.download_link)
        self.request=requests.get(self.current_repourl)

        with open("./{}.zip".format(repository_name),"wb") as folder:
            folder.write(self.request.content)

    def downloadAndExtractRepo(self,repository_name):

        print("\n[*] Downloading {} Repository...".format(repository_name))
        self.current_repourl="{}{}/{}".format(self.userurl,repository_name,self.download_link)
        self.request=requests.get(self.current_repourl)

        with open("./{}.zip".format(repository_name),"wb") as folder:
            folder.write(self.request.content)
            folder.close()


        print("[*] Extracting {} Repository...".format(repository_name))
        repozip=zipfile.PyZipFile('./{}.zip'.format(repository_name))
        repozip.extractall()
        repozip.close()
        print("[*] Downloaded and Extracted {} Repository...".format(repository_name))
        os.remove('./{}.zip'.format(repository_name))

    def displayLicense(self,repo_name):

        license_present=False
        license_displayed=False
        print("\n\n")
        
        try:
            repopath="./{}-main/".format(repo_name)
            for repofile in os.listdir(repopath):
                if "LICENSE" in repofile:
                    license_present=True
        except FileNotFoundError:
            option=input("Do you want ot Download and Extract {} Repository First (y/n) >> ".format(repo_name))
            if option=='y':
                self.downloadAndExtractRepo(repo_name)
                license_displayed=False
            elif option=='n':
                print("\nLicense Can't Be Displayed as Repository Not Present in Local Device.")
            
            else:
                print("Type 'y' or 'n'.")

        if license_present==True:
            while license_displayed==False:
                try:
                    repopath="./{}-main/".format(repo_name)
                    for repofile in os.listdir(repopath):
                        if "LICENSE" in repofile:
                            with open(os.path.join(repopath,repofile),'r') as f:
                                print(f.read())
                                f.close()
                                license_displayed=True

                except FileNotFoundError:
                    option=input("Do you want ot Download and Extract {} Repository First (y/n) >> ".format(repo_name))
                    if option=='y':
                        self.downloadAndExtractRepo(repo_name)
                        license_displayed=False
                    elif option=='n':
                        print("\nLicense Can't Be Displayed as Repository Not Present in Local Device.")
                        break
                    else:
                        print("Type 'y' or 'n'.")
        else:
            print("License Not Present in Repository")
            




