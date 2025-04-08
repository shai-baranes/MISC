# classes_advanced.py

''' Protected members (single underscore "_" as a prefix): accessed only by the class it’s sub-classes (Child classes). '''
''' Private members (single underscore "__" as a prefix): accessed only in the main class.'''


class human:
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender

	def displaygender(self):
		print(self.gender)

	def displayname(self):
		print(self.name)


class student(human):
    def __init__(self, grade, name, gender):
    	super().__init__(name, gender)
    	self.grade = grade
        # self.name = name
        # self.gender = gender
 
    def displaygrade(self):
        print(self.grade)
 
 
obj = student(6, "Bob", "Male")
obj.displayname()
obj.displaygrade()
obj.displaygender()



# -------------------------------Using dict of dicts---------------------------------------

''' instantiate new users from a given dictionary '''
''' appears that it is possible only if you stich it into array/list [] of objects...'''

class User:
    def __init__(self, first, last, age, id):
        self.firstname = first
        self.lastname  = last
        self.age       = age
        self.id       = id


my_dict = {
    'User1': {'id': 'id001', 'firstname': 'Shai', 'lastname': 'Baranes', 'age': 51},
    'User2': {'id': 'id002', 'firstname': 'Hadas', 'lastname': 'Golan', 'age': 48},
    'User3': {'id': 'id003', 'firstname': 'Jimi', 'lastname': 'Cohen', 'age': 8}
}




users1 = []
for user in my_dict:
    params    = my_dict[user]
    obj = User(params['firstname'], params['lastname'], params['age'], params['id'])
    users1.append(obj) # new


# --------------------------------Using list of dicts-----------------------------


''' instantiate new users from a given dictionary '''
''' appears that it is possible only if you stich it into array/list [] of objects...'''

class User:
    def __init__(self, first, last, age, id):
        self.firstname = first
        self.lastname  = last
        self.age       = age
        self.id       = id

dicts_list = [
    {'id': 'id001', 'firstname': 'Shai', 'lastname': 'Baranes', 'age': 51},
    {'id': 'id002', 'firstname': 'Hadas', 'lastname': 'Golan', 'age': 48},
    {'id': 'id003', 'firstname': 'Jimi', 'lastname': 'Cohen', 'age': 8}
]





users2 = []
for user in dicts_list:
    obj = User(user['firstname'], user['lastname'], user['age'], user['id'])
    users2.append(obj) # new




try:
    print(User1.lastname) # :( not working
except Exception as e:
    print(e)
finally:
    print(obj.lastname) # last stored object


[print(f"First = {user.firstname}, Last = {user.lastname}, Age = {user.age}") for user in users1]First = Shai, Last = Baranes, Age = 51
# First = Hadas, Last = Golan, Age = 48
# First = Jimi, Last = Cohen, Age = 8
# [None, None, None]



# ----------------------------------


# ----------------------------------


''' unpack simple single dictionary to class '''
# https://codereview.stackexchange.com/questions/171107/python-class-initialize-with-dict


class User:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value) # bulk set attributes (self.key1 = value1; self.key2 = value2)
            # self.key = value # this is not working! :(


p1 = User(first_name='Shai', last_name='Baranes')
print(f"P1 first name: {p1.first_name}") # prints abs
print(f"P1 last name: {p1.last_name}")  # prints def
print()

# HOWTO init from a dict, notice how I unpack the dictionary to pass all the variables
p2 = User(**{'first_name':'Hadas', 'last_name':'Golan'})
print(f"P2 first name: {p2.first_name}") # prints abs
print(f"P2 last name: {p2.last_name}")  # prints def

# P1 first name: Shai
# P1 last name: Baranes

# P2 first name: Hadas
# P2 last name: Golan