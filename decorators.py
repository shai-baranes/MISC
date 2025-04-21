# from 'Bro Code': https://www.youtube.com/watch?v=ix9cRaBkVe0&t=29253s
# (extended code)
# Decorator = A function that extends the behavior of another function
#			  w/o modifying the base function
# 			  Pass the base function as an argument to the decorator

#		@add_sprinkles
#		get_ice_cream("vanilla")


from datetime import datetime
import time


################defining the decorators

def time_it(func):
	def wrapper():  #note that w/o adding kwargs to the wrapper, we only support functions that have no arguments
		t=datetime.now()
		func()
		print(f"{(datetime.now()-t).total_seconds()} seconds elapsed!")
	return wrapper


def add_sprinkles(func):
	def wrapper():
		print("*You add sprinkles 🎊*")
		func()
		print("*sprinkles are added 🎊*")
	return wrapper


# ------------------------------------------------


@time_it # we can have multiple decorators here
@add_sprinkles # note that w/o the wrapper, we're calling the function as soon as python sees this @func_name decorator
def get_ice_cream():
	time.sleep(1)
	print("Here is your ice cream 🍧")


get_ice_cream()
print()

# *You add sprinkles 🎊*
# Here is your ice cream 🍧
# *sprinkles are added 🎊*
# 1.000633 seconds elapsed!



def add_sprinkles_2(func):
	def wrapper(*args, **kwargs): # adding the arguments so the wrapper is able to pas is to the wrapped function
		print("*You add sprinkles 🎊*") # you can replace these lines w/ any desired funcs. (here for the initialization steps)
		func(*args, **kwargs)
		print("*sprinkles are added 🎊*") # you can replace these lines w/ any desired funcs. (here for collapsing/closure steps)
	return wrapper




@add_sprinkles_2 #
def get_ice_cream_2(flavor):
	print(f"Here is your {flavor} ice cream 🍧")


get_ice_cream_2("Vanilla")
# *You add sprinkles 🎊*
# Here is your Vanilla ice cream 🍧
# *sprinkles are added 🎊*