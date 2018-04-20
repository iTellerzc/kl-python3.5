#! /usr/bin/python3
#-*-coding:UTF-8-*-

path = './testa.txt'
f = open(path, 'w')
print('写入长度:',f.write('hello, world!'))
f = open(path, 'r')
print(f.read())
f = open(path, 'a')
print('写入长度:',f.write('append!'))
f = open(path, 'r')
print(f.read())
