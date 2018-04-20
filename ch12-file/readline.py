#! /usr/bin/python3
#-*-coding:UTF-8-*-

path = './lines.text'
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
	line = f.readline()
	if not line:
		break
	print('read line:', line)
f.close()
