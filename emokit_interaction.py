#Main class to be used on the input thread
#gets data and passes it to a blocking_queue
#adapted from emokit's example.py by Sam Findler

from emokit.emotiv import Emotiv
if platform.system() == "Windows":
    import socket #might fix breaking gevent on Windows
import gevent

class emokit_interaction:
  "class to use the emokit"
  headset = Emotiv()
  doorway = true
  
  def initialize(self):
    "to be called before using the Emotiv"
    gevent.spawn(this.headset.setup)
    gevent.sleep(100)
    return
    
  def queueData(self,blocking_queue):
    "put current data packet into blocking_queue"
    packet = this.headset.dequeue()
    blocking_queue.put(packet)
    return
    
  def close(self):
    "call this when done with the headset"
    self.headset.close()
    return
    
  def runForever(self,blocking_queue):
    "run until a keyboard interrupt causes it to stop"
    while doorway:
        self.queueData(blocking_queue)
    self.close()
    return
