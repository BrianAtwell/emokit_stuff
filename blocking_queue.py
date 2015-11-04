#special purpose blocking_queue that takes threshold number
#of elements, and won't allow a dequeue in any other size

from threading import Lock

class blocking_queue:
	list = [] #list contains the data that is being read in
	lock = Lock() #lock is self-explanatory
	threshold=0 #threshold is the maximum number of elements that the list will hold before kicking out members
	def __init__(self,threshold):
		self.threshold=threshold
	def put(self,y):
		"put an item in the list"
		self.lock.acquire() #test lock
		if(len(self.list) < self.threshold): #if bigger than threshold, kick out old item
			self.list.append(y)
		else:
			self.list.append(y)
			self.list.pop()
		self.lock.release() #release lock
		return
	def get(self):
		"get the entire list if it is big enough, else return the empty list"
		self.lock.acquire() #test lock
		a = []
		if(len(self.list) >=  self.threshold): #if under threshold, list isn't ready yet
			a = self.list 
			self.list = [] #reset list to empty once data has been gotten
		self.lock.release() #release lock
		return a
	def get_size(self):
		"atomically get the size of the list"
		self.lock.acquire()
		a = len(self.list)
		self.lock.release()
		return a
