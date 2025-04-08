# threading.py
# from linked-in course

import threading  # note that it is still the same process and we also have the multi-processing python option
import time


def longSquare1(num):
	time.sleep(1)
	return num**2

# long duration function
print([longSquare1(n) for n in range(0,5)])
# [0, 1, 4, 9, 16]

# ========================================

def longSquare2(num, results):
	print(f"func initiated with arg = {num}")
	time.sleep(1)
	results[num] = num**2




# although we may have delays, we can still run other computations in parallel!
results1 = {} # added dictinary so we can get the results from the threads
t1 = threading.Thread(target = longSquare2, args = (1,results1))
# t1 = threading.Thread(target = longSquare, args = (1,)) # adding ',' to the func argument to show python it is a tuple
t2 = threading.Thread(target = longSquare2, args = (2,results1))
# t2 = threading.Thread(target = longSquare, args = (2,))

t1.start()
t2.start()

t1.join() # checks to see if the thread has completed execution yet, and pauses until execution completes
t2.join()

# and now to get the results :)

print(results1)


# ===================================================

# Now adding the threads into a list

results2 = {} # added dictinary so we can get the results from the threads

threads = [threading.Thread(target = longSquare2, args=(n,results2)) for n in range(0,10)] # much faster than waiting one at the time
[t.start() for t in threads]
[t.join() for t in threads]
print(results2)


# results1:

# func initiated with arg = 1
# func initiated with arg = 2
# {1: 1, 2: 4}


# results2:
# func initiated with arg = 0
# func initiated with arg = 1
# func initiated with arg = 2
# func initiated with arg = 3
# func initiated with arg = 4
# func initiated with arg = 5
# func initiated with arg = 6
# func initiated with arg = 7
# func initiated with arg = 8
# func initiated with arg = 9
# {0: 0, 1: 1, 3: 9, 2: 4, 4: 16, 5: 25, 7: 49, 6: 36, 9: 81, 8: 64}




