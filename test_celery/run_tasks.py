from __future__ import absolute_import
from send import *
from .receive import recv 
from .receiver2 import recv2 
import time

print("initialize")
send_p()
# send_p()


# at this time, our task is not finished, so it will return False
# print ('Task finished? ', result.ready())
# print ('Task result: ', result)
# sleep 10 seconds to ensure the task has been finished

time.sleep(3)
# now the task should be finished and ready method will return True
# print ('Task finished? ', result.ready())
recv2()
print("am i alive?")
recv()
print("2nd task is alive too")

# print ('Task result: ', result)
