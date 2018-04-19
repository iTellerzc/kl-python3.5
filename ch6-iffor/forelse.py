#! /usr/bin/python3
#-*-coding:UTF-8-*-

names=['a','b']
for name in names:
	if name=='c':
		print('hit ', name)
		break
	print('name:',name)
else:
	print('not hit')
print('结束循环')