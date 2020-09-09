---
title: 'Enjoying with Git'
date: 2020-09-09
permalink: /posts/2020/09/working_with_git/
tags:
  - review
  - cheat sheet
---

I am loving to manage the codes or the works as well as possible. That's the thing! In this blog I would like to show you about how to work with Git in general. Let's do it!

Git
------

**What is Git?** Git is a distributed revision control and source code management system with an emphasis on speed<sup>[1](https://www.tutorialspoint.com/git/index.htm)</sup>. Historically, Git is initially used for the development of Linux by Linus Torvald and then currently being widely used for managing almost all of the codes for making sure the project can be distributed to the team properly and making easily used for the collaboration. Currently, Git is a free software distributed under the terms of the GNU General Public License version 2<sup>[1](https://www.tutorialspoint.com/git/index.htm)</sup>.  Before we turn into the Git, let's talk about Version Control System (VCS)!



## Version Control System

**Version Control System (VCS)** is a software that helps software developer to work together and maintain a complete history of their work<sup>[2](https://www.tutorialspoint.com/git/git_basic_concepts.htm)</sup>. According to [tutorialspoint.com](https://www.tutorialspoint.com/git/git_basic_concepts.htm), generally, there are some functions of VCS, they are:

1. Allows developers to work simultaneously.
2. Does not allow overwriting each other's changes.
3. Maintains a history of every version.



## The basic workflow of Git

Here is the simple basic workflow of Git:

<center><b>Create/Modify file[s] from the working directory</b></center>

<center><b>Add the files to the staging area</b></center>

<center><b>Perform commit operation</b></center>

done!

You have to be familiar with these operations, because you will use that workflow for every changes that you have done. 



## The configurations

The first thing after you install Git to your computer, you need to introduce your self into Git so that Git knows you and record your name for every things that you do in the projects.

You can use these examples to configure your identity to Git

```bash
$ git config --global user.name "Your Name Comes Here"
$ git config --global user.email you@yourdomain.example.com
```

and changing "`Your Name Comes Here`" and "`you@yourdomain.example.com`" with your name and email.

## Working with a new project

If you want to crate a new project, you can firstly make a folder, for the example `mkdir project` and type this command `git init` after you get in the folder (`cd project`). These are the all commands:

```bash
$ mkdir project
$ cd project
$ git init
```

Git will reply

```bash
Initialized empty Git repository in .git/
```

or if you have a project that has been created before, you can simply use `git init` in the project folder.

*Next...*

If you have been finished your work, you can add the modified or created file[s] to the staging area by using

```bash
$ git add .
```

or if you want to add a specific file, you can add it individually, for the example:

```bash
$ git add example.py
```

After that, the files (modified/created version) are now stored in a temporary staging area. You can permanently store the contents in the repository with

```bash
$ git commit -m "your description of the updated or created files / somethings that you want to remember for each commit"
```

## Cheat sheet

That make easy! If you are lazy to use the complete command, you can simply using `alias` to get the minimized version of the commands<sup>[3](https://bitsofco.de/git-aliases-for-lazy-developers/),[4](https://stackoverflow.com/questions/1838873/visualizing-branch-topology-in-git/11594406)</sup>. Check it out!

```bash
# Git
alias gi="git init && gac 'Initial commit'"

alias gs="git status"
alias glog='git log --graph --all --decorate'
alias gac="git add . && git commit -m" # + commit message

alias gp="git push" # + remote & branch names
alias gpo="git push origin" # + branch name
alias gpom="git push origin master"

alias gl="git pull" # + remote & branch names
alias glo="git pull origin" # + branch name
alias glom="git pull origin master"

alias gb="git branch" # + branch name
alias gc="git checkout" # + branch name
alias gcb="git checkout -b" # + branch name

# git visualizing
alias graph1="git log --all --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(auto)%d%C(reset)'"
alias graph2="git log --all  --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(auto)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)'"
alias graph3="git log --all  --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset) %C(bold cyan)(committed: %cD)%C(reset) %C(auto)%d%C(reset)%n''          %C(white)%s%C(reset)%n''          %C(dim white)- %an <%ae> %C(reset) %C(dim white)(committer: %cn <%ce>)%C(reset)'"
```

## Additional References

These are some references that might be helpful for you:

1. [git-scm.com](https://git-scm.com/docs/gittutorial)
2. [tutorialspoint.com](https://www.tutorialspoint.com/git/git_basic_concepts.htm)
3. [bitsofco.de](https://bitsofco.de/git-aliases-for-lazy-developers/)
4. [stackoverflow.com](https://stackoverflow.com/questions/1838873/visualizing-branch-topology-in-git/11594406)
5. [gitignore](https://www.toptal.com/developers/gitignore)
6. [Git and Github (Web Programming UNPAS Playlist)](https://www.youtube.com/watch?v=lTMZxWMjXQU&list=PLFIM0718LjIVknj6sgsSceMqlq242-jNf) (Youtube playlist in Indonesian version)

