#! /usr/bin/python3
#-*-coding:UTF-8-*-

import pickle

d = dict(name='iTeller_zc', age=28)
print(pickle.dumps(d))
try:
	f_name = open('./dump.txt','wb')
	pickle.dump(d, f_name)
finally:
	f_name.close()