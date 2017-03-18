from flask import Flask
from github import Github
import base64
import sys


app = Flask(__name__)

#print sys.argv[1]

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/<filename>")
def get_RepoAndFile(filename):
      
    a = str(sys.argv[1]).split('https://github.com/')
    b = str(a[1])
    github = Github()
    
    g = github.get_user('Manasi670430')
    repository = g.get_repos()


    for repo in repository:
        
        if(repo.full_name==b):
            try:

                file =  repo.get_contents(filename)
                contentFile = base64.decodestring(file.content)
                return str(contentFile)
    
            except:
                return 'Invalid File..'
    
       
            
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
