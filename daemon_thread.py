# daemon thread = a thread that runs in the background, not important for the program to run
# 				your program will not wait for daemon threads to complete before exiting.
# 				non-daemon threads cannot normally be killed, it stays alive until task is complete.

# 				ex. background tasks, garbage collection, waiting for input, long runnig proccesses


# from 'Bro Code' https://www.youtube.com/watch?v=XKHEtdqhLK8&t=21211s

import threading
import time

def timer():
	print()
	print()
	count = 0
	while True:
		time.sleep(1)
		count+=1
		print(f"logged in for: {count} seconds")


x = threading.Thread(target=timer, daemon=True)
# x = threading.Thread(target=timer)
x.start()

# x.setDaemon(True)  # option, as log as it's before the thread is running

print(x.isDaemon()) # to know wheather it is a Daemon thread or not

answer = input("Do you wish to exit?")


