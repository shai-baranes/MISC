# from 'Code Bro': https://www.youtube.com/watch?v=ix9cRaBkVe0&t=27571s

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data (@staticmethod)
# Class methods = Best for class-level data or require access to the class itself (@classmethod)


# def header_creator(text):
# 	print(" ", "#"*100, "\n", " #", " "*int((95-len(text))/2), text, " "*int((94-len(text))/2), "#", "\n", "", "#"*100)

def header_creator(text):
	print(f" {'#'*100}")	
	print(" #", " "*96, "#")
	print(" #", " "*int((95-len(text))/2), text, " "*int((94-len(text))/2), "#")
	print(" #", " "*96, "#")
	print("", "#"*100)


# header_creator("Operator Overloading: __add__ (& returning a Class)")



class Student:
	"""docstring for Student"""

	count = 0 # class variable (can be accessed without initiating an object - and not from instatiated object)
	total_gpa = 0

	def __init__(self, name, gpa):
		self.name = name
		self.gpa = gpa
		Student.count += 1
		Student.total_gpa += gpa

	
	#INSTANCE METHOD
	def get_info(self):
		return f"{self.name} {self.gpa}"


	@classmethod  #try getting the count without this cls method
	def get_count(cls):
		return f"Total # of students: {cls.count}"


	@classmethod
	def get_gpa_average(cls):
		if cls.count == 0:
			return 0
		else:
			return f"Average GPA: {cls.total_gpa/cls.count:.2f}"


	@staticmethod
	def BMI_calc(weight, height):
		return 0 if weight == 0 else round(height/weight**2, 2)


	@staticmethod
	def is_student_in_class(name):
		valid_students = ["Spongebob", "Patrick", "Sandy"]
		return name in valid_students








student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4)


print(Student.get_count()) # Total # of students: 3
print(Student.count) # 3
print(Student.get_gpa_average()) # Total # of students: 3

print(f'Spongebob is {"in" if Student.is_student_in_class("Spongebob") else "not in"} class')
print(f'Shai is {"in" if Student.is_student_in_class("Shai") else "not in"} class')
print(Student.is_student_in_class("Spongebob"))
print(Student.is_student_in_class("Shai"))





  #################################################################################################### 
  #                                 CS50 Harry Potter Singleton Class                                # 
  ####################################################################################################


import random



class Hat:
	houses = ["Slytherin", "Grifendor", "c-house", "d-house"]

	@classmethod
	def sort(cls):
		return random.choice(cls.houses)



print(Hat.sort())




# note that if I run only the selected text using the last Sublime feature, I need to temporarily add random as global within the class
# e.g. 'class Hat: 	global random'



  #################################################################################################### 
  #                            Setter Protecting Decorator: 'Harry Potter'                           # 
  ####################################################################################################




print("\nClass setter getter property decoration ")
class Student:
	def __init__(self, name, house, patronus):
		# if not name: # moving the init check to name setter
		# 	raise ValueError("Missing name") # my customed Exception (when string is empty: "")
		# if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]: # moving the init check to house 'setter'
		# 	raise ValueError("Invalid house") # my customed Exception (when string is empty: "")
		self.name = name # note that if 'self._name = name' then it won't go through the setter inspection & error handling!
		self.house = house
		self.patronus = patronus

	def __str__(self):
		return f"name = {self.name}, house = {self.house}, patronus = {self.patronus}"

	# def get_student(self): # TBD?
	# 	return {name: self.name, house: self.house}


	@property # name getter
	def name(self):
		return self._name

	@name.setter # name setter
	def name(self, name):
		if not name:
			raise ValueError("Missing name") # my customed Exception (when string is empty: "")
		self._name = name

	@property # house getter
	def house(self):
		return self._house

	@house.setter # house setter
	def house(self, house):
		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise ValueError("Invalid house") # my customed Exception (when string is empty: "")
		self._house = house



	def charm(self):
		match self.patronus:
			case "Stag":
				return "🐴"
			case "Otter":
				return "🦦"
			case "Jack Russel terrier":
				return "🐶"
			case _:
				return "🩼"



	@staticmethod
	def get(name, house, patronus):
		return Student(name, house, patronus)

	# @classmethod # can also be like that (as prefered by the teacher)
	# def get(cls, name, house, patronus):
	# 	return cls(name, house, patronus)



try:
	student = Student.get("Harry", 'Gryffindor', 'Stag') # if I wanted to make it from input and more complex
	student = Student("Harry", 'Gryffindor', 'Stag') # or simply done:
	# student = Student.get("Harry", 'home', 'Stag')
except Exception as e:  # if error, then prints either "Invalid House" or "Missing name"
	print(e)
else:

	print("Expecto Patronus!")
	print(student.charm())

	print(student)

try:
	student.house = "my house" # invalid house
except Exception as e:  # if error, then prints either "Invalid House" or "Missing name"
	print(e)
finally:
	student.house = "Slytherin" # now it works!
	print(f"After successful update: {student}")



 ####################################################################################################
 #                                                                                                  #
 #                        Operator Overloading: __add__ (& returning a Class)                       #
 #                                                                                                  #
 ####################################################################################################

print()
class Vault:

	def __init__(self, galleons=0, sickles=0, knuts=0):
		self.galleons = galleons
		self.sickles = sickles
		self.knuts = knuts

	def __str__(self):
		return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"


	def calc_knuts(self):
		return (self.galleons + (self.sickles+ self.knuts*10)*10) * 10


	def __add__(self, other):
		return Vault(self.galleons + other.galleons, self.sickles + other.sickles, self.knuts + other.knuts)



potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)


new_vault = potter+weasley