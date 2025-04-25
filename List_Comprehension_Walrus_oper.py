# List Comprehension - Python Simplified / Maria
# now from https://www.youtube.com/watch?v=SNq4C988FjU
# also incorporating the Walrus operation below

bits = [False, True, False, False, True, False, False, True]


# what I remembered: (both provide same output)
new_bits = [1 for bit in bits if bit is True]
new_bits = [1 for bit in bits if bit == True]
# ['1', '1', '1']


smart_new_bits = [1 if bit is True else 0 for bit in bits]
# smart_new_bits = [1 if bit == True else 0 for bit in bits] # same
# [0, 1, 0, 0, 1, 0, 0, 1]

# ==================================================================


fruits = ["apple", "bananas", "straberries"]

[print(fruit) for fruit in fruits]
# apple
# bananas
# straberries

# ==================================================================

fruits = ["apple", "bananas", "straberries"]
upper_fruits = [fruit.upper() for fruit in fruits]
# ['APPLE', 'BANANAS', 'STRABERRIES']

# ==================================================================


my_string = "HelloMyNameIsShai"
my_string = "".join([i for i in my_string])
# my_string = "".join([i for i in my_string])
# >>> 'HelloMyNameIsShai'

new_string = "".join([i if i.islower() else f" {i}" for i in my_string])[1:] # slicing out the space char at the beginning
# 'Hello My Name Is Shai'


temp_string = "".join([i if i.islower() else f"_{i.lower()}" for i in my_string])[1:] # slicing out the space char at the beginning
# 'hello_my_name_is_shai'



new_string = "".join([i if i.islower() else f" {i.lower()}" if i in "MNI" else f" {i}" for i in my_string])[1:]
new_string = "".join([i if i.islower() else f" {i.lower()}" if i in ["M", "N", "I"] else f" {i}" for i in my_string])[1:] # ame as above
# 'Hello My name is Shai'
# ["N", "I"]

# ==================================================================

# list comprehension from @TechWithTim
# https://www.youtube.com/watch?v=twxE0dEp3qQ


options = ["any", "albany", "apple", "world", "hello", ""]
valid_strings = [string for string in options if len(string)>1 if string[0]=="a" if string[-1]=="y"]
# ['any', 'albany']

# same as: (more readable!)
valid_strings = [
	string
	for string in options 
	if len(string)>1 
	if string[0]=="a" 
	if string[-1]=="y"
]


#---------

# flattenig Matrix (list of lists)
matrix = [[1, 2, 3], [4, 5, 3], [6, 7, 8]]
flattened = [num for rows in matrix for num in rows]
# >> [1, 2, 3, 4, 5, 3, 6, 7, 8]

categories = ["Even" if number % 2 == 0 else "Odd" for number in range(10)] # similar to above existing example
# ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']


#---------
# building a 3D list (neted lists)
lst = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)] # we could use "i" instead of "_" but we do nothing with that i so can be "_"
# >> [[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]], [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]], [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]], [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]], [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]]

# otherwise we had to do it this way:

lst = []

for a in range(5):
	l1=[]
	for b in range(5):
		l2=[]
		for num in range(5):
			l2.append(num)
		l1.append(l2)
	lst.append(l1)


#--------- now w/ function call

def square(x):
	return x**2

squared_numbers = [square(x) for x in range(10)]
# squared_numbers = [x**2 for x in range(10)] # same as this
# squared_numbers = [pow(x,2) for x in range(10)] # same as this
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# list comprehension
l2 = [x * y for x in range(3) for y in range(3) if x>y] # [0, 0, 2]
# l2 = [x * y for x in range(3) for y in range(3)] # [0, 0, 0, 0, 1, 2, 0, 2, 4]


# --------------------------------------


# all() vs. any()
new_arr = [1,2,-1,-2]

if any(n>1 for n in new_arr):
	print("the array has number > 1")

# --

if all(n>1 for n in new_arr):
	print("all array elements are > 1")
else:
	print("not all array elements are > 1")



#---------


# utilizing If/Else one liner as part of the list comprehension:


"Positive" if num >=0 else "Negative" # this is an if/else statement within one line

my_list = [-1,5,-6,7,-9,0]

print(["Positive" if num >=0 else "Negative" for num in my_list])
# ['Negative', 'Positive', 'Negative', 'Positive', 'Negative', 'Positive']




# --------------------#############-----------------

# walrus operator:
# not same but nice and practical (from 'Bro Code': 'https://www.youtube.com/watch?v=XKHEtdqhLK8&t=16060s' )

# assign values to variables as part of a lrger expression


foods = list()
# foods = []
while True:
	food = input("What food do you like? ('q' to quit): ")
	if food.lower() == 'q':
		break
	foods.append(food)

# and in a shorter Walrus way:

while (food := input("Again, what food do you like? ('q' to quit): ")).lower() != 'q':
	foods.append(food)





# --------------------#############-----------------


# Additional examples for list/dict comprehensions (taken from Harvard CS50):


# dict comprehension:
students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)
# {'Hermione': 'Gryffindor', 'Harry': 'Gryffindor', 'Ron': 'Gryffindor'}




# creating a list of dicts using list comprehension:
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

list_of_students = [{"name": student, "house": house} for student, house in zip(students, houses)]

print(list_of_students)
# [{'name': 'Hermione', 'house': 'Gryffindor'}, {'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Ron', 'house': 'Gryffindor'}, {'name': 'Draco', 'house': 'Slytherin'}]

