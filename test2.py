from push_github import push_to_repo_branch
from github import Github
from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()
push_to_repo_branch("qoutes.json", "qoutes.json", "CJcrispy/E-zone", "main", "CJcrispy", os.getenv('GITHUB_TOKEN'))

