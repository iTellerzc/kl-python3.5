#! /usr/bin/python3
#-*-coding:UTF-8-*-
num=7
if num%2==0:
	if num%3==0:
		print("你输入的数字可以整除2和3")
	elif num%4==0:
		print("你输入的数字可以整除2和4")
	else:
		print("你输入的数字可以整除2，但不能整除3和4")
else:
	if num%3==0:
		print("你输入的数字可以整除3，单不能整除2")
	else:
		print("你输入的数字不能整除2和3")