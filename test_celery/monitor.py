from __future__ import absolute_import
from send import *
from .receive import recv 
from .receiver2 import recv2 
import time

print("initialize")

recv()
print("2nd task is alive too")

# print ('Task result: ', result)
