#example of grabbing data through the blocking_queue,
#just prints the first table from each data grab to the file 'temp_data.txt'
#by Sam Findler

from blocking_queue import blocking_queue
from emokit_interaction import emokit_interaction

import threading

def generate_data(emokit,blocking_queue):
  "use emokit to put data into blocking_queue"
  emokit.initialize()
  emokit.queueData(blocking_queue)

def grab_some_data(emokit,blocking_queue,file):
  "get data for 10 iterations than close the headset"
  i = 0
  while(i < 10):
    file.write(blocking_queue.get()[0] + "\n")
    i = i+1
  emokit.doorway=false
  
f = open('temp_data.txt','w')

#create new emokit_interaction
emokit = emokit_interaction()

#make the blocking_queue take 1 second of data from the headset
#the headset runs at 128hz
blocking_queue = blocking_queue(128)  

#create a producer thread with target=generate_data
producer_thread = threading.Thread(target=gernerate_data,args=(emokit,blocking_queue)

#create a consumer thread with target=grab_some_data
consumer_thread = threading.Thread(target=grab_some_data,args=(emokit,blocking_queue,f)
