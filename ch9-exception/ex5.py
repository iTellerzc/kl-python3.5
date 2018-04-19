#! /usr/bin/python3
#-*-coding:UTF-8-*-
def devision_fun(x, y):
	return x/int(y)

def exp_fun(x,y):
	return devision_fun(x, y) * 10

def main(x, y):
	exp_fun(x, y)

main(2, 0)