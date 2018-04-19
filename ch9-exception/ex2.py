#! /usr/bin/python3
#-*-coding:UTF-8-*-
def mult_exception(x,y):
	try:
		a = x/y
		b = name
		
	except (ZeroDivisionError, NameError, TypeError) as e:
		print(e)
	#except NameError:
	#	print('name错误')
mult_exception(2,'')