#! /usr/bin/python3
#-*-coding:UTF-8-*-

path = './testw.txt'
f = open(path, 'w')
print('写入长度:',f.write('hello, world!'))
f = open(path, 'r')
print(f.read())