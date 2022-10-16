'''
测试文件
切换到“我的分支”
步骤：
创建分支:git branch wylbranch
查看分支：git branch
切换到我的分支：git checkout wylbranch

#=====================
切换到自己的分支之后
开发自己的代码
1、提交之前，拉取项目上主分支最新的代码：git pull或者执行git pull -origin master
如果有冲突，自己想办法解决
2、提交已经写好并自测过的代码：git add 已经写好的代码.py     
3、git commit -m '代码的文字说明'
4、提交到自己的分支上：git push --set-upstream prigin wylbranch

后面你的经理或者CTO会登录gitlab进行代码审查、合并
'''