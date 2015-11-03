from threading import Lock

class blocking_queue:
	x = 1
	list = []
	lock = Lock()
	threshold=0
	def __init__(self,threshold):
		self.threshold=threshold
	def put(self,y):
		self.lock.acquire()
		if(len(self.list) < self.threshold):
			self.list.append(y)
		else:
			self.list.append(y)
			self.list.pop()
		self.lock.release()
		return
	def get(self):
		self.lock.acquire()
		a = []
		if(len(self.list) >=  self.threshold):
			a = self.list
			self.list = []
		self.lock.release()
		return a
	def get_size(self):
		self.lock.acquire()
		a = len(self.list)
		self.lock.release()
		return a
