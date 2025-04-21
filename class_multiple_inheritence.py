# from 'Bro Code': https://www.youtube.com/watch?v=ix9cRaBkVe0&t=07h00m02s
# w/ fathers and grandpas


class Animal:
	def __init__(self, name="koko"):
		self.name = name


	def eat(self):
		print(f"{self.name} is eating")

	def sleep(self):
		print(f"{self.name} is sleeping")



class Prey(Animal):
	def flee(self):
		print(f"{self.name} is fleeing")

class Predator(Animal):
	def hunt(self):
		print(f"{self.name} is hunting")


class Rabbit(Prey):
	pass

class Hawk(Predator):
	pass

class Fish(Prey, Predator):
	pass




rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")


rabbit.flee()
fish.hunt()
fish.flee()

rabbit.eat()
fish.sleep()

