# YouTube tip:
# Include the timestamp at the end of the video URL using the format &t=XhYmZs. "X" is the number of hours, "Y" is the number of minutes, and “Z” is the number of seconds.


# YouTube Bro Code at:
# https://www.youtube.com/watch?v=XKHEtdqhLK8&t=14654s


# method chaining = calling multiple methods sequentially
					# each call performs an action on the same object and return self (need to be implemeted in such a way)



class Car:

	def turn_on(self):
		print("You start the engine")

	def drive(self):
		print("You drive the car")

	def brake(self):
		print("You step on the brake")

	def turn_off(self):
		print("You turn off the engine")



car = Car()

car.turn_on()
car.drive()

# You start the engine
# You drive the car

# note that ">> car.turn_on().drive()" will not work here


print()

class Car2:

	def turn_on(self):
		print("You start the engine")
		return self

	def drive(self):
		print("You drive the car")
		return self

	def brake(self):
		print("You step on the brake")
		return self

	def turn_off(self):
		print("You turn off the engine")
		return self



car2 = Car2()

car2.turn_on().drive() # chained methods
car2.brake().turn_off()

# # this also works:
# car2.turn_on()
# car2.drive()
