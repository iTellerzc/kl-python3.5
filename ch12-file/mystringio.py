#! /usr/bin/python3
#-*-coding:UTF-8-*-

from io import StringIO

# io_val = StringIO()
# io_val.write('hello')
# print('say:', io_val.getvalue())
io_val = StringIO('hello\nworld!\nwelcome!')
while True:
	line = io_val.readline()
	if line == '':
		break
	print('line value:', line.strip())
