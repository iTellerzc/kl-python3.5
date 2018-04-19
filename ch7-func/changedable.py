#! /usr/bin/python3
#-*-coding:UTF-8-*-

#可变参数函数
def personinfo(arg, * vartuple):
	print(arg)
	for var in vartuple:
		print('我属于不定长参数部分：', var)
	return

personinfo('tracy')
personinfo('tract',21,'nanjing')
