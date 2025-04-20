# from 'Bro Code': https://www.youtube.com/watch?v=XKHEtdqhLK8&t=05h58m19s

# multiprocessing = running tasks in parallel on different CPU cores, bypass GIL used for threading.
# 				  multiprocessing = better for cpu bound tasks (heavy cpu usage)
# 				  multithreading = bettwe for io bound tasks (waiting around)


from multiprocessing import Process, cpu_count
import time
from datetime import datetime


def counter(num):
	count = 0
	while count < num:
		count+=1




def main():
	print(cpu_count()) # 12 (I can run up-to 12 parallel processes --> 11 seconds)
	start_time = time.perf_counter()
	start_time2 = datetime.now()
	# when sharing, it took 22 seconds for the entire process combined (and 16 seconds when having 4 parallel processes)
	a = Process(target=counter, args=(1000000000/2,)) # --> 30 seconds
	b = Process(target=counter, args=(1000000000/2,)) # --> 30 seconds
	a.start()
	b.start()

	a.join()
	b.join()

	print(f"finished in: {time.perf_counter() - start_time} seconds")
	print(f"finished in: {datetime.now() - start_time2} -> datetime module")




# def main():
# 	start_time = time.perf_counter()
# 	a = Process(target=counter, args=(100000000,)) # --> 3 seconds
# 	# a = Process(target=counter, args=(1000000000,)) # --> 30 seconds
# 	a.start()

# 	a.join()

# 	print(f"finished in: {time.perf_counter() - start_time} seconds")



if __name__ == "__main__":
	main()




