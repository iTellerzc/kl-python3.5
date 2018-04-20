#! /usr/bin/python3
#-*-coding:UTF-8-*-

import os

path = './rename.txt'
f = open(path, 'w')
f.close()
os.rename('rename.txt','rename2.txt')