#! /usr/bin/python3
#-*-coding:UTF-8-*-

class DefaultInit(object):
	def __init__(self):
		print('我是不带参数的构造方法__init__')

	def __init__(self, param):
		print('我是带一个参数的构造方法__init,参数:', param)
	#def show(self):
	#	print('我是类定义中的方法，需要通过实例化对象调用')

#test = DefaultInit('hello', 'world')
test = DefaultInit()
print('类实例化结束')
#test.show()
