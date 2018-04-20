#! /usr/bin/python3
#-*-coding:UTF-8-*-

import json
data = {'age':28, 'name':'iTeller_zc'}
json_str = json.dumps(data)
print('python原始数据：', data)
print('JSON对象：', json_str)

data2 = json.loads(json_str)
print('data2[name]:', data2['name'])
print('data2[age]:', data2['age'])

#写入数据
with open('./json.txt','w') as f:
	json.dump(data, f)
#读取数据
with open('./json.txt', 'r') as f:
	print('load json:',json.load(f))