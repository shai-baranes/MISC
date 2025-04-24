# # ------ from Harvard full python course-----------


def temp():
	# my way to catch both the error type and error text upon any exception, to later be able to catch and handling it appropriately!
	while True:
		try:
			x=int(input("(mine) What's x? "))
			print(f"x is {x}")
		except Exception as e: # cathing any type of exception
		    print(f"{type(e).__name__}: {e}")
		else:
			break

	# ValueError: invalid literal for int() with base 10: 





	# herein a good practice to loop until getting a valid integer, from CS50 Harvard class on Python basics.
	# URL: https://www.youtube.com/watch?v=nLRL_NcnK-4&t=4h31m41s

	while True:
		try:
			x=int(input("What's x? "))
			print(f"x is {x}") # break can also come after the print (we get here only if havcing no Exception)
		except ValueError: # catching a specifiuc type of exception
		    print("x is not an integer")
		except AssertionError:  # not relate here!!!
			pass
		else:
			break
		# finally:


# adding it into a function (note TBD)
# with additional code to enable it run from asserttion pytest suite!
def main(my_val=None):
	x = get_int(my_val)
	# x = get_int("koko")
	print(f"x is {x}")


def get_int(value=None):
	while True:
		try:
			if not value:
				x=int(input("What's x? "))
			else:
				x=int(value)
		except ValueError: # catching a specifiuc type of exception
		    print("x is not an integer")
		    # print(f"debug - do we get here? value = {value}")
		    if value:
			    return f'out of the loop, value = {value}'
		    	# break
		else:
			break
	return x


if __name__ == "__main__":
	main()





# ----------------



def get_int2():
	while True:
		try:
			x=int(input("What's x? "))
			print(f"x is {x}") # break can also come after the print (we get here only if havcing no Exception)
		except ValueError: # catching a specifiuc type of exception
		    print(f"x is not an integer")
		else:
			break
	return x
		# finally: