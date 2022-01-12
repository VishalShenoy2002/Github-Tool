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





