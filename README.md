# emokit_stuff
Basic work for the Brain Controller Interface project.

Mainly stuff to get data to train neural networks and stuff to use that data and build an eeg analysis program.

Installing emokit on windows (not fully tested):

  1. install python, pip
  2. use pip to install pywinhid, pycrypto and gevent 
  3. may need to pip install socket as well
  4. Donwload the repo from openyou/emokit (the other ones don't seem to work on windows, there are some slight code changes)
  5. cd into emokit/python and run "python setup.py"
  6. run "python example.py" with the device plugged in to insure that it works 
