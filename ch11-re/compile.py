#! /usr/bin/python3
#-*-coding:UTF-8-*-

import re

re_tel = re.compile(r'^(\d{3})-(\d{3,8})$')

print(re_tel.match('010-12345').groups())
print(re_tel.match('010-9090').groups())