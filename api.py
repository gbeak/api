from github import Github

g = Github("c810e1051547fa0ca620155dd969b825d2004906")

for repo in g.get_repos():
    print(repo.name)

