#! /usr/bin/python3
#-*-coding:UTF-8-*-

path = './byte.txt'
# f = open(path, 'w')
# f.write('Hello')
# f = open(path, 'r')
# b = f.read(1)
# while b :
# 	print('read single:', b)
# 	b = f.read(1)
# f.close()

f = open(path)
while True:
	b = f.read(1)
	if not b:
		break
	print('read single:', b)
f.close()

