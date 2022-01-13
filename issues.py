from imports import *


class Issues():

    def __init__(self, username):

        self.username = username

        self.mainurl = "https://github.com/{}/".format(self.username)
        self.issueurl = "{}/issues"

        self.request = requests.get(self.mainurl, allow_redirects=True)

        self.soup = BeautifulSoup(self.request.content, "html.parser")

        self.issues = {}

    def listIssues(self, reponame):

        self.url='{}{}'.format(self.mainurl,self.issueurl.format(reponame))

        self.request=requests.get(self.url,allow_redirects=True)
        self.soup=BeautifulSoup(self.request.content,"html.parser")

        c="Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title"
        
        for i in self.soup.find_all("a",class_=c):
            issuename=i.text
            issuelink=i['href']
            self.issues[issuename]=issuelink

        return self.issues

    def readIssue(self,issuename):

        for issue in self.issues:
            if issue==issuename:
                url="https://github.com{}".format(self.issues[issue])
                webbrowser.open_new_tab(url)

        
