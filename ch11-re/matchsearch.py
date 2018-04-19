#! /usr/bin/python3
#-*-coding:UTF-8-*-

import re

line='Cats are smarter than dogs'

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
	print('use match, the match string is:', matchObj.group())
else:
	print('no matcing str!')

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
	print('use search, the match string is:', matchObj.group())
else:
	print('no match str!')