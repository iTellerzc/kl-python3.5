#! /usr/bin/python3
#-*-coding:UTF-8-*-

class MyClass(object):
	i = 123
	def __init__(self,name):
		self.name = name

	def f(self):
		return 'hello,' + self.name

user_class = MyClass('iTeller_zc')
print('调用类的属性:', user_class.i)
print('调用类的方法:', user_class.f())