#! /usr/bin/python3
#-*-coding:UTF-8-*-
total=0
def sum(arg1,arg2):
	total=arg1+arg2
	print('函数内是局部变量:',total)
	return total

def totalprint():
	print('total的值是：',total)
	return total

print('函数的求和结果：', sum(10,20))
totalprint()
print('函数外是全局变量：', total)