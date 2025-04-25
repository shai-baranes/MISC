# Harvard (CS50), URL: https://www.youtube.com/watch?v=nLRL_NcnK-4&t=50500s

# def header_creator(text):
# 	print(f" {'#'*100}")	
# 	print(" #", " "*96, "#")
# 	print(" #", " "*int((95-len(text))/2), text, " "*int((94-len(text))/2), "#")
# 	print(" #", " "*96, "#")
# 	print("", "#"*100)


# header_creator("Proper 'Function' Documentation")




 ####################################################################################################
 #                                                                                                  #
 #                                   Type Hints & Applicable Tool                                   #
 #                                                                                                  #
 ####################################################################################################
# CS50 URL: https://www.youtube.com/watch?v=nLRL_NcnK-4&t=14h18m14s



# apply: > mypy type_hints.py (package that need pip install)

def meow(n: int) -> str:
	return "meow\n" * n # if I want to return a string
	# for _ in range(n): # won't work if we give it str (without casting it to int post input)
	# 	print("meow")
		# yield "meow"



number: int = int(input("Number: ")) # TBD (int also here?)
meows: str = meow(number)

# for   i in meows: # if using Generator (by 'yield' from function)
# 	print(i)
print(meows, end="")


# > mypy type_hints.py (results w/ the following):
# 		type_hints.py:29: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]                                
#		Found 1 error in 1 file (checked 1 source file)                                                                                    
#		(note that it can only work if we provide it w/ type-hints - TBD try to automate it per commit)



 ####################################################################################################
 #                                                                                                  #
 #                                  Proper 'Function' Documentation                                 #
 #                                                                                                  #
 ####################################################################################################
# now w/ proper documentation:
# note that there are tool to extract your data and to create from it a proper documentation (3rd party tools)
# TBD investigate such tools...

def meow(n: int) -> str:
	"""
	Meows n times.

	:param n: Number of times to meow
	:type n: int
	:raise TypeError: If n is not an int
	:return: A string on n meows, one per line
	:rtype: str
	"""

	return "meow\n" * n # if I want to return a string





number: int = int(input("Number: ")) # TBD (int also here?)
meows: str = meow(number)

print(meows, end="")



 ####################################################################################################
 #                                                                                                  #
 #                                     List / Dict Unpacking...                                     #
 #                                                                                                  #
 ####################################################################################################




# basic unpack on list
list = [1,2,3,4,5]
print(*list) # 1 2 3 4 5
print(*list, sep=', ', end="") # 1, 2, 3, 4, 5



