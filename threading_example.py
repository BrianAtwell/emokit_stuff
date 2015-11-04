#this example demonstrates how to use the blocking_queue in
#a threaded environment

#it also demonstrates the way that because of the 'threshold'
#some data points will be lost in a more or less continuous data set.
#by Sam Findler



import threading
from blocking_queue import blocking_queue
#import blocking_queue data structure

bq = blocking_queue(100) 
#blocking_queue is set with a threshold, which is the number of elements in
#the queue before it will accept a get, it is also the 
#max number of elements in the blocking_queue


def getter(s):
	"attempts to get a list of elements from blocking_queue s"
	a = s.get()

	#get returns [] if it could not get data yet, hence the loop
	while(a == []): 
		a = s.get()
	print str(a) + "\n"
	return a
def putter(s,p):
	"attempts to put an element p on blocking queue s"
	s.put(p)
	return
def run1(s):
	"put 1000 items on the queue"
	i = 0
	while(i < 1000):
		putter(s,i)
		i = i + 1
	return
def run2(s):
	"attempts to get 5 lists from the queue"
	i = 0
	while(i < 5):
		getter(s)
		i = i + 1
	return

thread1 = threading.Thread(target=run1,args=(bq,))
thread2 = threading.Thread(target=run2,args=(bq,))
thread1.start()
thread2.start()
