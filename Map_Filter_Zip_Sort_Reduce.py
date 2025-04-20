
################# Map

# ---
def multiply_by2(item): # fixed
	return item*2

map(multiply_by2, [1,2,3]) # <map object at 0x00000149688ED7E0> (iterable object) --> to view it, we have to turn it to a list
list(map(multiply_by2, [1,2,3])) # [2, 4, 6]
# ---


list(map(lambda i: i*2, [1,2,3])) # [2, 4, 6] as well



# another example from 'Code Bro': https://www.youtube.com/watch?v=XKHEtdqhLK8&t=17602s

store = [
		("shirt", 20.00),
		("pants", 25.00),
		("jacket", 50.00),
		("socks", 10.00),
]


to_NIS = lambda data: (data[0], data[1]*3.8)
to_NIS_2 = lambda data: (f"{data[0]}_NIS", data[1])


store_NIS = map(to_NIS, store) # arg1 = function, arg2 = data
# ('shirt', 76.0)
# ('pants', 95.0)
# ('jacket', 190.0)
# ('socks', 38.0)

store_NIS = map(to_NIS_2, store_NIS)
for line in store_NIS:
	print(line)
# ('shirt_NIS', 76.0)
# ('pants_NIS', 95.0)
# ('jacket_NIS', 190.0)
# ('socks_NIS', 38.0)


# can be coverted to a list:
print(list(map(to_NIS, store))) # [('shirt', 76.0), ('pants', 95.0), ('jacket', 190.0), ('socks', 38.0)]



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



# from 'Bro Code': https://www.youtube.com/watch?v=XKHEtdqhLK8


# filter(function, iterable)
friends = [
			("Rachel", 19),
			("Monica", 18),
			("'Phoebe", 17),
			("Joey", 16),
			("Chandler", 21),
			("Ross" , 20)
		  ]

age = lambda data: data [1] >= 18
drinking_buddies = list(filter(age, friends))
# [('Rachel', 19), ('Monica', 18), ('Chandler', 21), ('Ross', 20)]




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
# also refer to 'Bro Code': https://www.youtube.com/watch?v=XKHEtdqhLK8&t=18654s


simple_dict = {
	'a': 1,
	'b': 2,
	'c': 3,
}

my_dict = {key: value**2 for key, value in simple_dict.items()}
# {'a': 1, 'b': 4, 'c': 9}

cities_in_F = {
	'New York': 32,
	'Boston': 75,
	'Los Angeles': 100,
	'Chicago': 50,
}


# what we actually do is quite similar to mapping
cities_in_C = {key: round((value-32)*5/9, 2) for key, value in cities_in_F.items()}
# {
# 	'New York': 0.0,
# 	 'Boston': 23.89,
# 	 'Los Angeles': 37.78,
# 	 'Chicago': 10.0
# }




cities_in_C = {'_'.join(key.lower().split(" ")): round((value-32)*5/9, 2) for key, value in cities_in_F.items()}
# {
# 	'new_york': 0.0,
# 	 'boston': 23.89,
# 	 'los_angeles': 37.78,
# 	 'chicago': 10.0,
# }


weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "Cloudy"}

sunny_weather = {key: value for key, value in weather.items() if value == "sunny"}
# {'Boston': 'sunny', 'Los Angeles': 'sunny'}

weather_season = {key: "Summer"  if value == 'sunny' else "Winter"  for key, value in weather.items()}
# {
# 	'New York': 'Winter',
# 	'Boston': 'Summer',
# 	'Los Angeles': 'Summer',
# 	'Chicago': 'Winter',
# }

desc_cities = {key: ("WARM" if value >=20 else "COLD") for key, value in cities_in_C.items()}
# {
# 	'new_york': 'COLD',
# 	'boston': 'WARM',
# 	'los_angeles': 'WARM',
# 	'chicago': 'COLD',
# }


def check_temp(value):
	if value >=70:
		return "HOT"
	elif 69>= value >= 40:
		return "WARM"
	else:
		return "COLD"

cities_classified_temp = {key: check_temp(value) for key, value in cities_in_F.items()}
# cities_classified_temp = {key: value for key, value in cities_in_F.items()}

# {
# 	'New York': 'COLD',
# 	'Boston': 'HOT',
# 	'Los Angeles': 'HOT',
# 	'Chicago': 'WARM',
# }






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



################### Reduce

# from 'Code Bro': https://www.youtube.com/watch?v=XKHEtdqhLK8&t=18010s

import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y: x+y, letters)
# word = "HELLO"

numbers = [1,2,3,4,5]
factorial = functools.reduce(lambda x, y: x*y, numbers)
# factorial = 120