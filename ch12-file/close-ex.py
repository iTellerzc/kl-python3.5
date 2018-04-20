#! /usr/bin/python3
#-*-coding:UTF-8-*-

path = './close.txt'
try:
	f = open(path, 'w')
	f.write('hello, world!\n')
finally:
	if f:
		f.close()

path = './close.txt'
with open(path, 'w') as f:
	f.write('hello, world!\n')
