#! /usr/bin/python3
#-*-coding:UTF-8-*-
#99乘法表

row=1
print('99乘法表')
while row <= 9:
	ids=range(1,row+1);
	for id in ids:
		print('{}*{}={}\t'.format(id,row,id*row),end='')
	print()
	row += 1 
	