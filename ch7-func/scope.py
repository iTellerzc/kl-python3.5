#! /usr/bin/python3
#-*-coding:UTF-8-*-

x=50
def func(x):
	print('x等于',x)
	x=2
	print('局部变量x变为',x)
func(x)
print('x一直是',x)
