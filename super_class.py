# taken from 'Bro Code': https://www.youtube.com/watch?v=ix9cRaBkVe0&t=25684s
# allows you to extend the functionality of the inherited methods


# getting the common attributes into a Parent Class
import math

class Shape:
	def __init__(self, color, is_filled):
		self.color = color
		self.is_filled = is_filled

	# for extending functionality
	def describe(self):
		print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}\n")



class Circle(Shape):
	"""docstring for ClassName"""
	def __init__(self, color, is_filled, radius):
		super().__init__(color, is_filled)
		self.radius = radius
		# self.color = color
		# self.filled = filled

	def describe(self):
		print(f"It is a circle with radius = {self.radius} --> Area = {math.pi*self.radius**2:.2f}cm²")
		super().describe() # extending the functionality of the describe method


class Square(Shape):
	"""docstring for ClassName"""
	def __init__(self, color, is_filled, width):
		super().__init__(color, is_filled)
		# super(ClassName, self).__init__()
		self.width = width
		# self.color = color
		# self.is_filled = is_filled

	def describe(self):
		print(f"It is a square with width = {self.width} --> Area = {self.width**2}cm²")
		super().describe()


class Triangle(Shape):
	"""docstring for ClassName"""
	def __init__(self, color, is_filled, width, height):
		super().__init__(color, is_filled)
		# self.color = color
		# self.is_filled = is_filled
		self.width = width
		self.height = height
		

	def describe(self):
		print(f"It is a triangle with width = {self.width}, height = {self.height} --> Area = {self.width*self.height/2.0:.2f}cm²")
		super().describe()



circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

print(f"circle: color={circle.color}, is_filled={circle.is_filled}, radius={circle.radius}cm") # red
print(f"square: color={square.color}, is_filled={square.is_filled}, width={square.width}cm") # red
print(f"triangle: color={triangle.color}, is_filled={triangle.is_filled}, width={triangle.width}cm, height={triangle.height}cm") # red

print()

circle.describe()
square.describe()
triangle.describe()