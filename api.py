from github import Github

access_token = ""
g = Github(access_token)

for repo in g.get_repos():
    print(repo.name)

