#! /usr/bin/python3
#-*-coding:UTF-8-*-

def count():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs

f1,f2,f3 = count()
print('f1的执行结果:',f1())
print('f2的执行结果:',f2())
print('f3的执行结果:',f3())