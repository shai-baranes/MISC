# "Multi Threading" from 'Bro Code': https://www.youtube.com/watch?v=XKHEtdqhLK8&t=20398s

import threading
import time
from timeit import timeit
from datetime import datetime




# using threading, the below sequence shall elapse only 5 seconds instead of 12 seconds!
def eat_breakfast():
	time.sleep(3)
	print("You ate your breakfast")


def drink_coffee():
	time.sleep(4)
	print("You drunk your coffee")


def study():
	time.sleep(5)
	print("You finish studying")

t1 = datetime.now() # for timing the total runtime

x = threading.Thread(target=eat_breakfast, args=()) # note that if the target func consumes a single argument, you need to pass it in arge, with ',' --> args=(vlue,) so it to know that we're dealing with a tuple of arguments
# x = threading.Thread(target=eat_breakfast, args=()) # note that if the target func consumes a single argument, you need to pass it in arge, with ',' --> args=(vlue,) so it to know that we're dealing with a tuple of arguments
y = threading.Thread(target=drink_coffee, args=()) # ", args()" is optional (in this case it works the same with or without)
z = threading.Thread(target=study, args=())
x.start()
y.start()
z.start()


print(threading.active_count()) # 1 -->  4
print(threading.enumerate()) # [<_MainThread(MainThread, started 29248)>]
# --> [<_MainThread(MainThread, started 13848)>, <Thread(Thread-1 (eat_breakfast), started 32068)>, <Thread(Thread-2 (drink_coffee), started 33816)>, <Thread(Thread-3 (study), started 31708)>]


# note also that without the join (join to main thread), you can enter any prompt to execution console, e.g. check the num of active threads
x.join() # the join is essential in case you have dependency and want to continue only after a certain thread is finished!
y.join() # the join is essential in case you have dependency and want to continue only after a certain thread is finished!
z.join() # the join is essential in case you have dependency and want to continue only after a certain thread is finished!


print(f"{datetime.now() - t1} seconds elapsed") # 5 seconds

# You ate your breakfast
# You drunk your coffee
# You finish studying


## below is the conservative classic way:
# t1 = datetime.now()
# # in the below conventional way, we had to wait sequentially
# study()
# drink_coffee()
# eat_breakfast()
# print(f"{datetime.now() - t1} seconds elapsed") # 12 seconds


## You finish studying
## You drunk your coffee
## You ate your breakfast


