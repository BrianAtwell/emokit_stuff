# emokit_stuff
Basic work for the Brain Controller Interface project.

Mainly stuff to get data to train neural networks and stuff to use that data to build an eeg analysis program.

Installing emokit on windows:

  1. install python, pip, visual C++ from http://www.microsoft.com/en-us/download/details.aspx?id=44266
  2. add python and (optionally pip) to path
  3. use pip to install pywinusb, pycrypto and gevent 
  4. Download the emokit repo forked on my github
  5. cd into emokit-master/python and run "python setup.py"
  6. run "python example.py" with the device plugged in to insure that it works 
