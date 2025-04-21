# from 'Bro Code': https://www.youtube.com/watch?v=ix9cRaBkVe0&t=27976s

# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__, __add__, __lt__, __contains__, __getitem__
# 				  They are automatically called by many of Python'sbuilt-in operations.
# 				  They allow developers to define or customize the behavior of objects



class Student:

	def __init__(self, name, gpa):
		self.name = name
		self.gpa = gpa

	def __str__(self):
		return f"name: {self.name} gpa: {self.gpa}"


	def __eq__(self, other): # is equal ?
		return self.name == other.name


	def __gt__(self, other): # is greater than?
		return self.gpa > other.gpa

	def __lt__(self, other): # TBD
		return self.gpa < other.gpa



student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)


print(student1) # name: Spongebob gpa: 3.2
print(student1==student2)# False
print(student1>student2)# True



###################### ore advanced ##################



class Book(object):
	"""docstring for Book"""
	def __init__(self, title, author, num_pages):
		# super(Book, self).__init__()
		self.title = title
		self.author = author
		self.num_pages = num_pages

	def __str__(self):
		return f"{self.title} by {self.author}"


	def __eq__(self, other):
		return self.title == other.title and self.author == other.author

	def __lt__(self, other):
		return self.num_pages < other.num_pages

	def __gt__(self, other): # it appears that this deemed redundant having the above method!
		return self.num_pages > other.num_pages

	def __add__(self, other): # it appears that this deemed redundant having the above method!
		return f"{self.num_pages + other.num_pages} pages"

	def __contains__(self, keyword): # it appears that this deemed redundant having the above method!
		return keyword.lower() in self.title.lower() or keyword.lower() in self.author.lower()


	def __getitem__(self, key):
		if key == "title":
			return self.title
		if key == "author":
			return self.author
		if key == "num_pages":
			return self.num_pages
		return f"{key} was not found"




book1 = Book("The Hobbit", "JRR Tolkien", 310)
book2 = Book("Harry Potter", "JK Rowling", 223)
book3 = Book("The lion, the witch and the wardrobe", "CS Lewis", 172)
book4 = Book("The lion, the witch and the wardrobe", "CS Lewis", 172)


print(book1) # The Hobbit by JRR Tolkien
print(book2) # Harry Potter by JK Rowling
print(book3) # The lion, the witch and the wardrobe by CS Lewis

print(book3 == book4) # True

print(book2 < book3) # False
print(book2 > book3) # False
print(book2 + book3) # 395 pages (accumulated number of pages)


print("Lion" in book3) # True
print("JK" in book2) # True

print(book2["author"]) # JK Rowling
print(book2["title"]) # Harry Potter
print(book2["num_pages"]) # 223
print(book2["koko"]) # koko was not found