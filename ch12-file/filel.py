#! /usr/bin/python3
#-*-coding:UTF-8-*-

path = './testl.txt'
f = open(path, 'w')
print('写入长度:',f.write('hello, world!\n'))
f = open(path, 'r')
print(f.read())
f = open(path, 'a')
print('写入长度:',f.write('append!'))
f = open(path, 'r')
print(f.readlines())