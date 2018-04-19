#! /usr/bin/python3
#-*-coding:UTF-8-*-

from functools import partial

def mod(m,n):
	return m%n

mode_by_100 = partial(mod,100)

print('自定义函数：',mod(100,7))
print('调用偏函数:',mode_by_100(7))