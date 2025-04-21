# from 'Code Bro': https://www.youtube.com/watch?v=ix9cRaBkVe0&t=27571s

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data (@staticmethod)
# Class methods = Best for class-level data or require access to the class itself (@classmethod)


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

