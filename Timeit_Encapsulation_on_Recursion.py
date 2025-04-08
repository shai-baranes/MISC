# recursions.py

# use timeit to measure function runtime
# https://docs.python.org/3/library/timeit.html


import time
# import timeit  # in that case we need to call timeit.timeit()
from timeit import timeit

# Decorator!
def timeit_no_args(fn): # works on any function that doesn't require any argument.
    def inner_function():        
        print('Start')
        start_time = time.time()
        fn()
        print(f'Time elapsed in secs: {time.time() - start_time}')
    return inner_function








# @timeit1
# def greet():
# 	print('Hello!')


def EvenNums(num): # w/o check for input
	print(num)
	if num==2: # note that if you provide odd number, it never reach 2
		return num
	else:
		EvenNums(num-2)


# EvenNums(8)
# 8
# 6
# 4
# 2



def EvenNums(num): # w/input check w/my touch (to avoid printing the odd number)
	if num % 2 != 0:
		print("please enter an even number!")
	elif num==2: # note that if you provide odd number, it never reach 2
		# return num
		print(num)
	else:
		print(num)
		EvenNums(num-2)


EvenNums(8)
# 8
# 6
# 4
# 2

 
# @timeit # not good for recursions
def fibonacci_recursive(idx): # sum-up of 2 prior values
	if idx==0:
		return 0
	elif idx==1:
		return 1
	else:
		return fibonacci_recursive(idx-1) + fibonacci_recursive(idx-2)


# index: 0	1	2	3	4	5	6
# value: 0	1	1	2	3	5	8

fibonacci_recursive(6)  # fibonacci of a large number shall take long long time to compute
# 8



# @timeit
def fibonacci_iterative(idx):
	seq = [0, 1]
	for i in range(idx):
		seq.append(seq[-1]+seq[-2])
	return seq[-1]



print(f"\n{fibonacci_iterative(10)}")
# timeit.timeit(fibonacci_iterative(10))


# timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)



loop = 10 # number of iterations
# loop = 1000

result1 = timeit('fibonacci_iterative(35)', globals=globals(), number=loop) # code is executed in the global namespace
result11 = timeit(lambda: fibonacci_iterative(35), number=loop)
# 1.750001683831215e-05  # much much quicker!
result2 = timeit('fibonacci_recursive(35)', globals=globals(), number=loop)
result22 = timeit(lambda: fibonacci_recursive(35), number=loop)
# 1.9586382999550551


# result = timeit.timeit(lambda: test(n), number=loop)