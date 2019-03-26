
import requests
import os

response = requests.get('https://api.github.com/users/<repo_name>/repos').json()

for repo in response:
    url=str(repo['html_url'])
    cmd='git clone '+url
    os.system(cmd)
grepcmd='grep -r <pattern>'
os.system(grepcmd)
