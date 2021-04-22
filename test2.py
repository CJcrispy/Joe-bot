import github

#g = github.Github(token)
# or  
g = github.Github("CJcrispy", "Fightinggold20!")

repo = g.get_user().get_repo("E-zone")
file = repo.get_file_contents("/your_file.txt")

# update
repo.update_file("/your_file.txt", "update qoutes", "your_new_file_content", file.sha)