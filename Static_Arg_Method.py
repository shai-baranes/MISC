# Static & Instance Methods
# from linkedIn course


# without the static mode ('text' is self argument to the class)
class WordSet():
	def __init__(self):
		self.words = set() # empty set of words

	def addText(self, text):
		self.text = self.cleanText(text)
		for word in self.text.split():
			self.words.add(word) # adding word to the words set from init


	def cleanText(self, text): # note that self is not used in 'cleanText'
		self.text = text.replace('!', '').replace('.', '').replace(',', '').replace('\'', '') # chaining functions
		return self.text.lower()
		

# let's add to it a big block of text

wordSet = WordSet()
wordSet.addText('Hi, I\'m Ryan! Here is a sentence I want to add!')
wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)
# {'a', 'hi', 'to', 'sentence', 'another', 'is', 'i', 'add', 'here', 'want', 'ryan', 'im'}



# =========================now with Static Method===================

class WordSet():
	replacePuncs = ['\'', '!', '.', ','] # static variable (w/o self.)
	def __init__(self):
		self.words = set() # empty set of words

	def addText(self, text): # instance method
  		text = WordSet.cleanText(text) # 'WordSet.' instead of 'self.' due to te statuc 'cleanText'
  		for word in text.split():
  			self.words.add(word) # adding word to the words set from init

	def cleanText(text): # now it is a static method after removing the 'self'
		for punc in WordSet.replacePuncs:
			text = text.replace(punc, '')
		# text = text.replace('!', '').replace('.', '').replace(',', '').replace('\'', '') # chaining functions
		return text.lower()




# let's add to it a big block of text

wordSet2 = WordSet()
wordSet2.addText('Hi, I\'m Ryan! Here is a sentence I want to add!')
wordSet2.addText('Here is another sentence I want to add.')

print(wordSet2.words)
# {'a', 'hi', 'to', 'sentence', 'another', 'is', 'i', 'add', 'here', 'want', 'ryan', 'im'}



# ----

# As it is statuic, we could use it clean w/o having to instantuiate any class member
for punc in WordSet.replacePuncs:
	print(punc)

# '
# !
# .
# ,



# =========================now with decorator for Static Methods===================

class WordSet():
	replacePuncs = ['\'', '!', '.', ','] # static variable/argument
	def __init__(self):
		self.words = set() # empty set of words

	def addText(self, text):
		text = self.cleanText(text)
		for word in text.split():
			self.words.add(word) # adding word to the words set from init

	@staticmethod
	def cleanText(text): # static method w/o needing to align on the 'addText' method (python neefty trick)
		for punc in WordSet.replacePuncs:
			text = text.replace(punc, '')
		# text = text.replace('!', '').replace('.', '').replace(',', '').replace('\'', '') # chaining functions
		return text.lower()

# let's add to it a big block of text

wordSet3 = WordSet()
wordSet3.addText('Hi, I\'m Ryan! Here is a sentence I want to add!')
wordSet3.addText('Here is another sentence I want to add.')

print(wordSet3.words)
# {'a', 'hi', 'to', 'sentence', 'another', 'is', 'i', 'add', 'here', 'want', 'ryan', 'im'}