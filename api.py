from github import Github

g = Github("access_code")

for repo in g.get_repos():
    print(repo.name)

