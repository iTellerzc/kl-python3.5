#! /usr/bin/python3
#-*-coding:UTF-8-*-
#快速排序
def quicksort(L):
	qsort(L,0,len(L)-1)

def qsort(L, first, last):
	if(first<last):
		split=partition(L,first,last)
		qsort(L,first,split-1)
		qsort(L,split+1,last)

def partition(L, first, last):
	#选取列表的第一个元素为划分元素
	pivot=L[first]
	leftmark=first+1
	rightmark=last
	while True:
		while L[leftmark] <= pivot:
			#如果列表中存在于划分元素pivot相等的元素，让他位于left部分
			#以下检测用于划分元素pivot是列表中的最大元素时防止leftmark越界
			if leftmark == rightmark:
				break
			leftmark+=1
		while L[rightmark] >pivot:
			#这里不需要检测，划分元素pivot时列表中的最小元素时，rightmark自动停在first处
			rightmark -= 1
		if leftmark < rightmark:
			#此时，leftmark处的元素大于pivot,rightmark处的元素小于等于pivot，交换两者
			L[leftmark],L[rightmark] = L[rightmark], L[leftmark]
		else:
			break
	#交换first处的划分元素与rightmark处的元素
	L[first],L[rightmark]=L[rightmark],L[first]
	#返回划分元素pivot的最终位置
	return rightmark

num_list=[5,6,-4,3,7,11,1,2]
print('排序之前：' + str(num_list))
quicksort(num_list)
print('排序之后：' + str(num_list))