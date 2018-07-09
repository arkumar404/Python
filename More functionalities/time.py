import datetime
import time

list = []
for i in range(5):
    list.append(datetime.datetime.now())
    time.sleep(1)

for i in list:
    print(i)