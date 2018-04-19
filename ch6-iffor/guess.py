#! /usr/bin/python3
#-*-coding:UTF-8-*-

#规则：给定一个数字，猜对即终止，才超过该数提示大了，反之提示小了
import random

num=random.randint(1,100)
print('随机数：',num)
guess=0
while True:
	num_input=input('输入一个1到100的数字：')
	guess += 1
	if not num_input.isdigit():
		print('请输入数字')
	elif int(num_input)<0 or int(num_input)>=100:
		print('输入的数字在1-100之间')
	else:
		if num == int(num_input):
			print('恭喜猜对了，猜了%d次'% guess)
			break
		elif num>int(num_input):
			print('你猜小了')
		elif num<int(num_input):
			print('你猜大了')
		else:
			print('系统错误')
