# taken from: https://www.youtube.com/watch?v=XKHEtdqhLK8 ("Python Full Course for free" by 'Bro Code')

# def header_creator(text):
# 	print(f" {'#'*100}")	
# 	print(" #", " "*96, "#")
# 	print(" #", " "*int((95-len(text))/2), text, " "*int((94-len(text))/2), "#")
# 	print(" #", " "*96, "#")
# 	print("", "#"*100)


# header_creator("Any number of 'Positional'/'Named' arguments")





def add(*args): # note that you can replace args with any other name
	# total = 0
	# for arg in args:
	# 	total+=arg
	# return total
	return sum(args)



print(add(1,2,3))



# unpacking dict
def func(**kwargs): # note that you can replace kwargs with any other name
	for key, value in kwargs.items():
		if isinstance(value, str):
			print(f"Key: {key}, Value: {value}")
		elif isinstance(value, float):
			print(f"Key: {key}, Value: {value:.2f}")


def func2(dict):
	for key, value in dict.items():
		if isinstance(value, str):
			print(f"Key: {key}, Value: {value}")
		elif isinstance(value, float):
			print(f"Key: {key}, Value: {value:.2f}")





func(name = "shai", age = 53.453)
print()
func2({"name": "shai", "age": 53.453}) # this won't work



# def func2(a,b):
# 	print(f"Key: {a}, Value: {b:.2f}")


# func2(a = "shai", b = 53.453)


# note also that Emojies are enabled by WIN_BUTTON + SEMI-COLON :
# ❤️🤷‍♂️👌💕🤣






 ####################################################################################################
 #                                                                                                  #
 #                           Any number of 'Positional'/'Named' arguments                           #
 #                                                                                                  #
 ####################################################################################################


# more examples for CS50 Harvard class:
# URL: https://www.youtube.com/watch?v=nLRL_NcnK-4&t=53994s


# To support a variable number of positional arguments / named arguments

def f(*args, **qwargs):
	print("Positional:", args)


f(100, 50, 25)
# Positional: (100, 50, 25)

f(100, 50, 25, 7)
# Positional: (100, 50, 25, 7)


f(100) # we still preserve the comma to indicate that this is a tuple and not an isolated element
# Positional: (100,)


def f(*args, **qwargs):
	print("Named:", qwargs)

f(galleons = 100, sickles = 50, knuts = 25)
# Named: {'galleons': 100, 'sickles': 50, 'knuts': 25}


