from github import Github
from push_github import push_to_repo_branch
import os

# using an access token
g = Github(os.getenv('GITHUB_TOKEN'))

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", login_or_token=os.getenv('GITHUB_TOKEN'))

repo = g.get_repo("CJcrispy/E-zone")
contents = repo.get_contents("qoutes.json", ref="test")
repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch="main")

# push_to_repo_branch("site/qoutes.json", "qoutes.json", "CJcrispy/E-zone", "main", "CJcrispy", os.getenv('GITHUB_TOKEN'))