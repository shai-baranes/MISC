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