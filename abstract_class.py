# https://www.youtube.com/watch?v=XKHEtdqhLK8&t=15140s  (Bro Code)

# for check and balances
# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation (and in forced upon any inheriting class)


from abc import ABC, abstractmethod   # ABC = "Abstract Base Class"

# ------
class Vehicle(ABC):  # by adding ABC we prevent user from creating an objecy of the abstract class


	@abstractmethod # by defining an abstractmehid we enforce user to define implementation for 'go' per any inheriting class
	def go(self):
		pass


	@abstractmethod # now we also force them to implement the 'stop' method
	def stop(self):
		pass

# ------




class Car(Vehicle):

	def go(self):
		print("You drive the car")

	def stop(self):
		print("You stop the car")



class Motorcycle(Vehicle):

	def go(self):  # motorcycle class must implement the 'go' method! (same for car)
		print("You drive the motorcycle")

	def stop(self):  # motorcycle class must implement the 'stop' method!
		print("You stop the motorcycle")


# vehicle = Vehicle() # no doable once we make it an abstract class
car = Car()
motorcycle = Motorcycle()


# vehicle.go() # no doable once we make it an abstract class
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()