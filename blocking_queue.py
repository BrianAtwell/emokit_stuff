from threading import Lock 
 
class blocking_queue(): 
        x = 1 
        list = [] 
        lock = Lock() 
        def put(self,y): 
                self.lock.acquire() 
                self.list.append(y) 
                self.lock.release() 
                return self.list[0] 
        def get(self): 
                self.lock.acquire() 
                if(len(self.list) > 0): 
                        a = self.list 
                        self.list = [] 
                self.lock.release() 
                return a 
        def get_size(self): 
                self.lock.acquire() 
                a = len(self.list) 
                self.lock.release() 
                return a
