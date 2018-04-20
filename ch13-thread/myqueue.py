#! /usr/bin/python3
#-*-coding:UTF-8-*-

import threading
from time import sleep
import queue

class MyThread(threading.Thread):
	def __init__(self, threadId, name, q):
		threading.Thread.__init__(self)
		self.threadId = threadId
		self.name = name
		self.q = q

	def run(self):
		print('开启线程：', self.name)
		process_data(self.name, self.q)
		print('退出线程:', self.name)

def process_data(threadName, q):
	while not exitFlag:
		queueLock.acquire()
		if not workQueue.empty():
			data = q.get()
			queueLock.release()
			print('%s processing %s'%(threadName, data))
		else:
			queueLock.release()
		sleep(1)

def main():
	global exitFlag
	exitFlag = 0
	#创建新线程
	threadList = ['Thread-1', 'Thread-2', 'Thread-3']
	nameList = ['one', 'two', 'three', 'four', 'five']
	threads = []
	threadId = 1

	#创建新线程
	for tName in threadList:
		thread = MyThread(threadId, tName, workQueue)
		thread.start()
		threads.append(thread)
		threadId += 1
	
	#填充队列
	queueLock.acquire()
	for word in nameList:
		print('word', word)
		workQueue.put(word)
	queueLock.release()

	#等待队列清空
	while not workQueue.empty():
		pass

	#通知线程是退出的时候了
	exitFlag = 1

	#等待所有线程完成
	for t in threads:
		t.join()

	print('退出主线程')


if __name__ == '__main__':
	queueLock = threading.Lock()
	workQueue = queue.Queue(10)
	main()