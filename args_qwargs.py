#TBD to be added to the full tutorial script output



def add(*args):
	# total = 0
	# for arg in args:
	# 	total+=arg
	# return total
	return sum(args)



print(add(1,2,3))



# unpacking dict
def func(**kwargs):
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