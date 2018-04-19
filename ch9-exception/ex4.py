#! /usr/bin/python3
#-*-coding:UTF-8-*-
def use_finally(x,y):
	try:
		a = x/y
	except Exception as e:
		print(e)
	else:
		print('else')
	finally:
		print('finally execute!')

use_finally(2,1)