import random
import string

# string.punctuation: !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
# string.digits: 0123456789
# string.ascii_letters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ



chars = f" {string.punctuation}{string.digits}{string.ascii_letters}"
chars = list(chars)
key = chars.copy()
random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")
# chars: [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# key: [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


plain_text = input("Enter a message to encrypt: ")
coded_text = ""

for letter in plain_text:
	index = chars.index(letter) # index is a very important capability in all non set/dict collections (as in data-frames)
	coded_text+=key[index]
	# coded_text.append(key[index]) # this is not working :(


print(f"encryped text: {coded_text}")


decoded_text = ""



for letter in coded_text:
	index = key.index(letter) # index is a very important capability in all non set/dict collections (as in data-frames)
	decoded_text+=chars[index]
	# coded_text.append(key[index]) # this is not working :(


print(f"decripted text: {decoded_text}")