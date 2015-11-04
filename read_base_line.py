#this file contains the function you call to get the
#users base-line values.  It takes about a second.
#it is stored in the data item base_lines.base_lines
#also contains utilities to save and load the base_lines from a file

class base_lines:
  base_lines #a dictionary containing the base_line readings
  
  def get_base_lines(self, blocking_queue):
    "should be the first function called for each person using the device"
    list = blocking_queue.get()
    F7 = 0
    FC5 = 0
    F3 = 0
    AF3 = 0
    F4 = 0
    FC6 = 0
    F8 = 0
    T7 = 0
    T8 = 0
    P7 = 0
    P8 = 0
    O1 = 0
    O2 = 0
    
    i = 0
    while(i < 128): #add up all the values of the various sensors
      F7 = F7 + list[i]['F7']['value']
      FC5 = FC5 + list[i]['FC5']['value']
      F3 = F3 + list[i]['F3']['value']
      AF3 = AF3 + list[i]['AF3']['value']
      F4 = AF4 + list[i]['AF4']['value']
      FC6 = FC6 + list[i]['FC6']['value']
      F8 = F8 + list[i]['F8']['value']
      T7 = T7 + list[i]['T7']['value']
      T8 = T8 + list[i]['T8']['value']
      P7 = P7 + list[i]['P7']['value']
      P8 = P8 + list[i]['P8']['value']
      O1 = O1 + list[i]['O1']['value']
      O2 = O2 + list[i]['O2']['value']
    
    #average those values
    F7 = F7 / 128
    FC5 = FC5 / 128
    F3 = F3 / 128
    AF3 = AF3 / 128
    F4 = AF4 / 128
    FC6 = FC6 / 128
    F8 = F8 / 128
    T7 = T7 / 128
    T8 = T8 / 128
    P7 = P7 / 128
    P8 = P8 / 128
    O1 = O1 / 128
    O2 = O2 / 128
    
    #put them into a dictionary where the key = name of sensor
    self.base_lines = {'F7' : F7, 'FC5' : FC5, 'F3' : F3, 'AF3' : AF3, 'F4' : F4, 'FC6' : FC6, 'F8' : F8, 'T7' : T7, 'T8' : T8, 'P7' : P7, 'O1' : O1, 'O2' : O2}
    
  save_base_lines(filename):
    "open filename and save the base_line_readings there"
    file = open(filename,'w')
    file.write(self.base_lines['F7'] + '\n')
    file.write(self.base_lines['FC5'] + '\n')
    file.write(self.base_lines['F3'] + '\n')
    file.write(self.base_lines['AF3'] + '\n')
    file.write(self.base_lines['F4'] + '\n')
    file.write(self.base_lines['FC6'] + '\n')
    file.write(self.base_lines['F8'] + '\n')
    file.write(self.base_lines['T7'] + '\n')
    file.write(self.base_lines['T8'] + '\n')
    file.write(self.base_lines['P7'] + '\n')
    file.write(self.base_lines['P8'] + '\n')
    file.write(self.base_lines['O1'] + '\n')
    file.write(self.base_lines['O2'] + '\n')
    file.close()
  
  read_base_lines(filename):
    "open filename and get the baseline readings from there"
    file = open(filename,'r')
    F7 = int(file.readline())
    FC5 = int(file.readline())
    F3 = int(file.readline())
    AF3 = int(file.readline())
    F4 = int(file.readline())
    FC6 = int(file.readline())
    F8 = int(file.readline())
    T7 = int(file.readline())
    T8 = int(file.readline())
    P7 = int(file.readline())
    P8 = int(file.readline())
    O1 = int(file.readline())
    O2 = int(file.readline())
    self.base_lines = {'F7' : F7, 'FC5' : FC5, 'F3' : F3, 'AF3' : AF3, 'F4' : F4, 'FC6' : FC6, 'F8' : F8, 'T7' : T7, 'T8' : T8, 'P7' : P7, 'O1' : O1, 'O2' : O2}
    file.close()
