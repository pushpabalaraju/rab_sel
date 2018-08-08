from __future__ import absolute_import
from .receive import * 
import time

print("initialize")
for i in range(3):
	send_p()
print("this is after send")
Wk1=recv.delay() 
status = Wk1.ready()
print("----- {} ".format(status))
print("this is after receiver 1 without delay")
time.sleep(5)
status = Wk1.ready()
print("----- {} ".format(status))
# b=Wk1.get()
# print("---rsults-- {} ".format(b.backend))
print("this is after receiver 1 after delay")
recv2.delay()
print("this is after receiver2")
