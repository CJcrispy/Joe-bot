from push_github import push_to_repo_branch
from github import Github
from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()
username = "Cjcrispy"
password = "Fightinggold20!"

# url to request
# url = f"https://api.github.com/users/{username}"
url = f"https://api.github.com/repos/CJcrispy/E-zone/contents/qoutes.json"

headers = {'Authorization': os.getenv('GITHUB_TOKEN')}
payload = {'message':'Mark', 'content': 'mark@bearer.sh' , 'sha': 'dd8884da8c4587fb725705a6eaa0db98bd39a66b'}
response = requests.put(url, headers=headers ,json=payload)
print(response)
# authenticate to github
# g = Github(username, password)

# user_data = requests.get(url).json()

# pprint(user_data)

# get the authenticated user
# user = g.get_user()
# for repo in user.get_repos():
#     print_repo(repo)