#! /usr/bin/python3
#-*-coding:UTF-8-*-

import fileinput

path = './input.txt'
# f = open(path, 'w')
# f.write('Hello')
# f = open(path, 'r')
# b = f.read(1)
# while b :
# 	print('read single:', b)
# 	b = f.read(1)
# f.close()

# f = open(path)
# for line in f:
# 	print('line is:', line)
# f.close()
for line in fileinput.input(path):
	print('line is:', line)
