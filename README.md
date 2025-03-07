# Carrot_Project
Final project for spring semester of 2025 at Deree ACG, Engineering practices

# Some Git commands

One of the main features of git in order to work with a group is 'Branch'

To see the concept of branch go see [This youtube video](https://www.youtube.com/watch?v=hwP7WQkmECE)

To see actual use of branch go see [this youtube video](https://www.youtube.com/watch?v=QV0kVNvkMxc)

- To update the code on pc : "git pull"
- To add modification : "git add \<path of modified file\>" (if it's a folder it will add all modified files in this folder)
- To commit (AKA prepare to upload) : "git commit -m \<Super description\>"
- To see some important info : "git status" (you can basically do it every time you do a git command this is really good)
- To push (AKA upload) : "git push"
- To change branch : "git switch \<name of branch\>" or "git checkout <name of branch"
- To create a new branch : "git branch \<name of branch\>"
- To merge branches : "git merge \<branch to import\>" in the growing branch
- To list all the existing branches : "git branch -a"

# Some good practices :

- Always be only one modifying code on a "branch" (if not : some work -maybe your- is lost)
- When browsing/changing between branches, ALWAYS do a "git pull" in the terminal : it permit to update the version on your pc, otherwise, if you do some modifications without doing "git pull" before there will be a lot of problems (like all your work you just did disapear because you will not be able to "git push")
- When you do a "git commit -m 'a super description of what have been done' ", the message have to be clear, it will help if there is some problem with git/github
- When you are leaving you pc, always push (=add + commit + push) your code : this save your work and everyone will be happy

