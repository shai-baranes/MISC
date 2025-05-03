# Harvard (CS50), URL: https://www.youtube.com/watch?v=nLRL_NcnK-4&t=50500s

# def header_creator(text):
# 	print(f" {'#'*100}")	
# 	print(" #", " "*96, "#")
# 	print(" #", " "*int((95-len(text))/2), text, " "*int((94-len(text))/2), "#")
# 	print(" #", " "*96, "#")
# 	print("", "#"*100)


# header_creator("Unpacking the 'list' values into the function!")




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
my_list = [1,2,3,4,5]
print(*my_list) # 1 2 3 4 5
print(*my_list, sep=', ', end="") # 1, 2, 3, 4, 5



def total_knuts(galleons, sickles, knuts):
	return (galleons *17 + sickles) *29 + knuts

coins = [100,50,25]






 ####################################################################################################
 #                                                                                                  #
 #                          Unpacking the 'list' values into the function!                          #
 #                                                                                                  #
 ####################################################################################################

print(total_knuts(100, 50, 25), "Knuts") # 50775 Knuts
print(total_knuts(coins[0], coins[1], coins[2]), "Knuts") # 50775 Knuts

# here comes the magic!
print(total_knuts(*coins), "Knuts") # 50775 Knuts

# -----------------------------------

names = ["galleons", "sickles", "knuts"]
coins = [100,50,25]

my_zip = list(zip(names, coins))
print(my_zip)
# [('galleons', 100), ('sickles', 50), ('knuts', 25)]


my_dict = {}

# getting assistance from zip to produce my dict()
for item in my_zip:
	my_dict[item[0]] = item[1]


my_dict2 = {}

# assuming both names & coins having the same length (len)
# & same results without the assistance by zip
for i in range(len(names)):
	my_dict2[names[i]] = coins[i]



print(my_dict)
# {'galleons': 100, 'sickles': 50, 'knuts': 25}

print(my_dict2) # same 
# {'galleons': 100, 'sickles': 50, 'knuts': 25}


# now using dictionary comprehension:
names = ["galleons", "sickles", "knuts"]
coins = [100,50,25]

print({name: coin for name, coin in zip(names,  coins)})
# {'galleons': 100, 'sickles': 50, 'knuts': 25}


 ####################################################################################################
 #                                                                                                  #
 #                        Unpacking the Dictionary values into the function!                        #
 #                                                                                                  #
 ####################################################################################################



def total_knuts(galleons, sickles, knuts):
	return (galleons *17 + sickles) *29 + knuts


my_dict = {'galleons': 100, 'sickles': 50, 'knuts': 25} # same order
print(*my_dict) # same as for my_dict2 -> getting you the dict keys
# galleons sickles knuts


print(total_knuts(**my_dict)) # for unpacking the dictionary values (by keys) into the function (note that order can be shuffled...)
# 50775






my_dict = {'sickles': 50, 'galleons': 100, 'knuts': 25} # shuffled order
print(total_knuts(**my_dict)) # and the result remains the same (the robust way to do it!)
# 50775

# same as passing the entire syntax:
print(total_knuts(galleons = 100, sickles = 50, knuts = 25)) # and the result remains the same (the robust way to do it!)
# 50775


# from python tricks book:
dict1 = {'Hermione': 'Gryffindor', 'Harry': 'Gryffindor'}
dict2 = {'Hermione': 'Gryffindor', 'Ron': 'Gryffindor'}
dict3 = {'Harry': 'Gryffindor', 'Ron': 'Gryffindor'}

gryffindors = {**dict1,** dict2,** dict3} # for combining dicts together and emit duplication if such exists
print(gryffindors) 
# {'Hermione': 'Gryffindor', 'Harry': 'Gryffindor', 'Ron': 'Gryffindor'}

