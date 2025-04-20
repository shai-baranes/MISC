# NAMELESS FUNCTIONS


# >>> (lambda a,b: a+b)(2,3)
# 5

func = lambda x: 3*x+1 

print(func(2))
# 7

full_name = lambda first_name, last_name: first_name.strip().title() + " " + last_name.strip().title()
# full_name = lambda first_name, last_name: f"{first_name.strip().title()} {last_name.strip().title()}"

print(full_name("   shai", " baranes  "))


scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur s C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]

# >>> help(scifi_authors.sort) # note for the "key" mentioning

# Help on built-in function sort:

# sort(*, key=None, reverse=False) method of builtins.list instance
#     Sort the list in ascending order and return None.
    
#     The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
#     order of two equal elements is maintained).
    
#     If a key function is given, apply it once to each list item and sort them,
#     ascending or descending, according to their function values.
    
#     The reverse flag can be set to sort in descending order.


scifi_authors.sort(key = lambda str: str.split(" ")[-1].lower())

print(scifi_authors)
# ['Douglas Adams', 'Isaac Asimov', 'Leigh Brackett', 'Ray Bradbury', 'Orson Scott Card', 'Arthur s C. Clarke', 'Robert Heinlein', 'Frank Herbert', 'H. G. Wells']


def build_quadratic_function(a, b, c):
	"""Returns the function f(x) = ax^2 + bx + c"""   # this is called: "doc string"
	return lambda x: a*x**2 + b*x + c


f = build_quadratic_function(2, 3, -5)
print(f(0))
# -5



build_quadratic_function(3, 0, 1)(2) # 3x^2+1 evaluated for x=2
# 13



help(build_quadratic_function)
# Help on function build_quadratic_function in module __main__:

# build_quadratic_function(a, b, c)
#     Returns the function f(x) = ax^2 + bx + c




# -----------------------------------

# Additional Lambda examples from 'Bro Code': 'https://www.youtube.com/watch?v=XKHEtdqhLK8&t=16870s'

double = lambda x: x*2
multiply = lambda x, y: x*y
add = lambda x, y: x+y
full_name = lambda first, last: f"{first.capitalize()} {last.capitalize()}"
age_check = lambda age: True if age >= 18 else False


double(7) # 14
multiply(2,5) # 10
full_name("shai", "baranes") # 'Shai Baranes'
age_check(17) # False



# sorting w/ lambda
students = [
			("Squidward", "F", 60),
			("Sandy", "A", 33),
			("Patrick", "D", 36),
			("Spongebob", "B", 20),
			("Mr. Krabs" ,"C", 78),
			]

grade = lambda items: items [1]
# grade = lambda lines: lines [1]
students.sort(key=grade)
for i in students:
	print(i)


## sort by grages:
# ('Sandy', 'A', 33)
# ('Spongebob', 'B', 20)
# ('Mr. Krabs', 'C', 78)
# ('Patrick', 'D', 36)
# ('Squidward', 'F', 60

age = lambda lines: lines [2]
students.sort(key=age, reverse=True)
for i in students:
	print(i)

## sort by ages (reversed)
# ('Mr. Krabs', 'C', 78)
# ('Squidward', 'F', 60)
# ('Patrick', 'D', 36)
# ('Sandy', 'A', 33)
# ('Spongebob', 'B', 20)


sorted_students = sorted(students, key=grade)
for i in sorted_students:
	print(i)

# ('Sandy', 'A', 33)
# ('Spongebob', 'B', 20)
# ('Mr. Krabs', 'C', 78)
# ('Patrick', 'D', 36)
# ('Squidward', 'F', 60)