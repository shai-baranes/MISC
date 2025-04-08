
################# Map

# ---
def multiply_by2(item): # fixed
	return item*2

map(multiply_by2, [1,2,3]) # <map object at 0x00000149688ED7E0> (iterable object) --> to view it, we have to turn it to a list
list(map(multiply_by2, [1,2,3])) # [2, 4, 6]
# ---


list(map(lambda i: i*2, [1,2,3])) # [2, 4, 6] as well


# ---

# list comprehension advanced

names = ["dalia", "moshe", "merav", "yoni", "oshrat", "shai"]

[name.capitalize() for name in names]

list(map(lambda name: name.capitalize(), names))
# ['Dalia', 'Moshe', 'Merav', 'Yoni', 'Oshrat', 'Shai']

# ---


def to_capitalize(str):
	return str.capitalize()

list(map(to_capitalize, names))
# ['Dalia', 'Moshe', 'Merav', 'Yoni', 'Oshrat', 'Shai']

# ---






################# Filter (Filter according to 'True' statements)

my_list = [1,2,3] # the odd number are '1' & '3'

def check_odd(item):
	return (item % 2) != 0
	# return item % 2 != 0 # also works


list(filter(check_odd, my_list))
list(filter(lambda item: item%2!=0, my_list)) # same as above
# [i for i in my_list if i%2!=0]  # same as by this list comprehension!
# [1, 3]








################# ZIP (coupling)

my_list = [1,2,3]
your_list = [10,20,30]


list(zip(my_list, your_list))
# [(1, 10), (2, 20), (3, 30)]


your_list = (10,20,30) # it can also be tuple and it doesn't matter!


list(zip(my_list, your_list))
# [(1, 10), (2, 20), (3, 30)]

#-------



# now for taking user names from one DB and taking the phone numbers from another list and combining the necessary data into a single list!

names = ["hadas", "shai"]
phone_number = ["0544651571", "0542253998"]
ids = ["032106304", "028854297"]

list(zip(ids, names, phone_number))
# [('032106304', 'hadas', '0544651571'), ('028854297', 'shai', '0542253998')]


# -------













################# Dictionary Comprehension

simple_dict = {
	'a': 1,
	'b': 2,
	'c': 3,
}


my_dict = {key: value**2 for key, value in simple_dict.items()}
# {'a': 1, 'b': 4, 'c': 9}


my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


duplicates = []
for value in my_list:
	if my_list.count(value)>1:
		if value not in duplicates:
			duplicates.append(value)

print(duplicates)
# ['b', 'n']

# also this list comprehention provides simiar results:  set() ans converting it to a list:
list({item for item in my_list if my_list.count(item)>1})




{char: my_list.count(char) for char in my_list}
# {'a': 1, 'b': 2, 'c': 1, 'd': 1, 'm': 1, 'n': 2}









################# SORT (advanced)

# List advanced sorting (using lambda)

my_list = [(10, -1), (4,3), (9,9), (0,2)]
my_list.sort()
print(my_list)
# [(0, 2), (4, 3), (9, 9), (10, -1)]

my_list = [(10, -1), (4,3), (9,9), (0,2)]

my_list.sort(key = lambda elem: elem[0]) # same effect as in my_list.sort()
# [(0, 2), (4, 3), (9, 9), (10, -1)]


my_list.sort(key = lambda elem: elem[1]) # sort on the 2nd element of each tuple here
print(my_list)
# [(10, -1), (0, 2), (4, 3), (9, 9)]



# sort(self, /, *, key=None, reverse=False)
#     Sort the list in ascending order and return None.



# -- more on SORT & SORTED---


 
# >>> help(list.sort) # same as >>> help([].sort)
#	Help on method_descriptor:
#	sort ( . . .)
#	L.sort (key=None, reverse=False) -> None - - stable sort IN PLACE


# 0-planet, 1-radius (size), 2-density, 3-distance from sun
planets = [
	("Mercury", 2440, 5.43, 0.395),
	("Venus", 6052, 5.24, 0.723),
	("Earth", 6378, 5.52, 1.000),
	("Mars", 3396, 3.93, 1.530),
	("Jupiter",	71492, 1.33, 5.210),
	("Saturn", 60268, 0.69, 9.551),
	("Uranus", 25559, 1.27, 19.213),
	("Neptune", 24764, 1.64, 30.070),
	]


# .sort() working on lists and not tuple/dicts
planets.sort() # sorting accoring to element[0] -> changes the list
# [('Earth', 6378, 5.52, 1.0), ('Jupiter', 71492, 1.33, 5.21), ('Mars', 3396, 3.93, 1.53), ('Mercury', 2440, 5.43, 0.395), ('Neptune', 24764, 1.64, 30.07), ('Saturn', 60268, 0.69, 9.551), ('Uranus', 25559, 1.27, 19.213), ('Venus', 6052, 5.24, 0.723)]


# sort by size.radius
planets.sort(key = lambda elem: elem[1], reverse = True) # like using the excel column sorting option
# size = lambda elem: elem[1]
# planets.sort(key = size, reverse = True)
# [
# 	('Jupiter', 71492, 1.33, 5.21),
# 	('Saturn', 60268, 0.69, 9.551),
# 	('Uranus', 25559, 1.27, 19.213),
# 	('Neptune', 24764, 1.64, 30.07),
# 	('Earth', 6378, 5.52, 1.0),
# 	('Venus', 6052, 5.24, 0.723),
# 	('Mars', 3396, 3.93, 1.53),
# 	('Mercury', 2440, 5.43, 0.395)
# ]



# sort by density
density = lambda elem: elem[2]
planets.sort(key = density, reverse = True)
# [
# 	('Earth', 6378, 5.52, 1.0), # the most dense planet
# 	('Mercury', 2440, 5.43, 0.395),
# 	('Venus', 6052, 5.24, 0.723),
# 	('Mars', 3396, 3.93, 1.53),
# 	('Neptune', 24764, 1.64, 30.07),
# 	('Jupiter', 71492, 1.33, 5.21),
# 	('Uranus', 25559, 1.27, 19.213),
# 	('Saturn', 60268, 0.69, 9.551),
# ]


help(sorted)
# Help on built-in function sorted in module builtins:

# sorted(iterable, /, *, key=None, reverse=False)
#     Return a new list containing all items from the iterable in ascending order.

data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)
print(sorted(data)) # works on imutable items like tuple
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(data) # sorted is not affecting theh source data
# (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)

