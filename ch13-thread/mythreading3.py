#! /usr/bin/python3
#-*-coding:UTF-8-*-

import threading
from time import sleep
from datetime import datetime

loops=[4,2]
date_time_format = '%y-%m-%d %H:%M:%S'

class MyThread(threading.Thread):
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)
		self.name = name
		self.func = func
		self.args = args

	def getResult(self):
		return sef.res

	def run(self):
		print('starting', self.name, 'at:', date_time_str(datetime.now()))
		self.res = self.func(*self.args)
		print(self.name, 'finished at:', date_time_str(datetime.now()))

def date_time_str(date_time):
	return datetime.strftime(date_time, date_time_format)

def loop(n_loop, n_sec):
	print('线程(', n_loop,') 开始执行：', date_time_str(datetime.now()), ', 先休眠（', n_sec, ')秒')
	sleep(n_sec)
	print('线程(', n_loop,') 休眠结束, 结束于：', date_time_str(datetime.now()))

def main():
	print('-----------所有线程开始时间：', date_time_str(datetime.now()))
	threads = []
	n_loops = range(len(loops))

	for i in n_loops:
		t =  MyThread(loop, (i, loops[i]), loop.__name__)
		threads.append(t)
	
	for i in n_loops:
		threads[i].start()

	for i in n_loops:
		threads[i].join()                #wait for all threads to finish

	print('-----------所有线程结束时间：', date_time_str(datetime.now()))

if __name__ == '__main__':
	main()