#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 16:08
# @Author  : 小海腾

# 本地仓库是自己电脑上的代码管理仓库，远程仓库是GitHub上的代码管理仓库

# git常用命令
# 1、用命令git add . 告诉Git，把文件添加到暂存区
# 2、用命令git commit -m '本次提交的说明' 告诉Git，把文件提交到本地仓库
# 为什么Git添加文件需要add，commit一共两步呢？因为commit可以一次提交很多文件，所以你可以多次add不同的文件
# git add命令实际上就是把要提交的所有修改放到暂存区（Stage），然后，执行git commit就可以一次性把暂存区的所有修改提交到分支
# 3、要随时掌握工作区的状态，使用git status命令。
# 4、如果git status告诉你有文件被修改过，用git diff可以查看修改内容。
# 5、git log命令显示从最近到最远的提交日志，我们可以看到3次提交，如果嫌输出信息太多，看得眼花缭乱的，可以试试加上--pretty=oneline参数
# 6、HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id
# 7、当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file
# 8、当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD <file>，就把暂存区的修改回退到工作区，第二步按第7步操作
# 9、把本地库的内容推送到远程，用git push命令
# 10、要克隆一个仓库，首先必须知道仓库的地址，然后使用git clone命令克隆

# ---------------------------------------------------------------------------------------------------------

# git分支管理
# HEAD指向当前的分支，当前的分支指向提交
# 1、查看分支：git branch命令会列出所有分支，当前分支前面会标一个*号
# 2、创建分支：git branch <name>
# 3、切换分支：git checkout <name>或者git switch <name>
# 4、创建+切换分支：git checkout -b <name>或者git switch -c <name>
# 5、合并某分支到当前分支：git merge <name>
# 6、删除分支：git branch -d <name>
