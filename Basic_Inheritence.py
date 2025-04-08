# my_class.py


class my_rectangle():
	def __init__(self, length=5, height=5):
		self.length = length
		self.height = height
		# self.area = self.length * self.height  # can be done either by init argument or by class method

	def area(self):
	# def area(self, length, height): # don't ask for length/height again (refer to init!)
		return self.length*self.height


class cube(my_rectangle):
	def __init__(self, length=6):
		super().__init__(length, length)
		# super().__init__(self, length, length) # once you use super, avoid self in __init__!


# -------------------------------------------------------


class quadriLateral:
    def __init__(self, a, b, c, d):
        self.side1=a
        self.side2=b
        self.side3=c
        self.side4=d

    def perimeter(self):
        p=self.side1 + self.side2 + self.side3 + self.side4
        print(f"perimeter={p}")




class rectangle(quadriLateral):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)


    def area(self):
        a = self.side1 * self.side2
        print(f"area of rectangle={a}")



class square(rectangle):
    def __init__(self, a):
        super().__init__(a, a)
        
    def area(self):
        a=pow(self.side1, 2)
        print('Area of Square: ', a)


