
import requests
import os

response = requests.get('https://api.github.com/users/<repo_name>/repos').json() #####getting the whole response containing every detail of all repos

for repo in response:
    url=str(repo['html_url'])######using this to parse the html url of therepo
    cmd='git clone '+url ####adding it to the git clone cmd
    os.system(cmd)########## executing the command
grepcmd='grep -r <pattern>'
os.system(grepcmd)
