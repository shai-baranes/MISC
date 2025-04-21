# from 'Code Bro': https://www.youtube.com/watch?v=ix9cRaBkVe0&t=30467s (write files section is followed by the read files sections)

# python writing files (.txt, .json, .csv)

# modes: 'w': write (overwrite), 'x': write only if file doesn't exists, 'a': append to file, 'r': read

txt_data = "I like Pizza!"

file1_path = "./Output/output_1.txt"
file2_path = "./Output/output_2.txt"

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]


# for output_1.txt
try: # like when we use 'x' and it appears that the file exists
	with open(file1_path, "x") as file: # like instantiating a file object: 'file = File()'
		file.write(txt_data) # we need to move to next line
		print(f"txt file '{file1_path}' was created")
except FileExistsError:
	print("That file already exists!")




# for output_2.txt
try: # like when we use 'x' and it appears that the file exists
	with open(file2_path, "w") as file: # like instantiating a file object: 'file = File()'
		for employee in employees:
			file.write(employee+ "\n")
		print(f"txt file '{file2_path}' was created")
except FileExistsError:
	print("That file already exists!")

# Eugene
# Squidward
# Spongebob
# Patrick

# ------------------------------------

import json

employees = {
	"name": "Spongebob",
	"age": 30,
	"job": "cook",
}


file_path = "./Output/output.json"

try:
	with open(file_path, "w") as file:
		json.dump(employees, file, indent=4)
		print(f"json file '{file_path}' was created")
except FileExistsError:
	print("That file already exists!")

# json file content w/o indent:
# {"name": "Spongebob", "age": 30, "job": "cook"} # json file content w/o indent

# json file content after adding the indent argument:
# {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "cook"
# }





# ------------------------------------


import csv

employees = [["Name", "Age", "Job"],
			["Spongebob", 30, "Cook"],
			["Patrick", 37, "Unemployed"],
			["Sandy", 27, "Scientist"]]



file_path = "./Output/output.csv"


try:
	with open(file_path, "w", newline="") as file: # adding argument "newline" to prevent empty row per row of data
		writer = csv.writer(file)
		for row in employees:
			writer.writerow(row)
		print(f"csv file '{file_path}' was created")
except FileExistsError:
	print(f"file '{file_path}' already exists!")

# Name,Age,Job
# Spongebob,30,Cook
# Patrick,37,Unemployed
# Sandy,27,Scientist




#################### now reading the files ########################

print()


file_path = "./Input/input.txt"

try:
	with open(file_path, "r") as file: # don't forget to put the 'r' in quotes: "r"
		content = file.read()
		print(content)
except FileNotFoundError:
	print(f"file '{file_path}' is missing")
except PermissionError:
	print(f"file '{file_path}' has no permission")


# -----------------------


file_path = "./Input/input.json"
print()
try:
	with open(file_path, "r") as file: # don't forget to put the 'r' in quotes: "r"
		content = json.load(file)
		print(content) #{'name': 'Spongebob', 'age': 30, 'job': 'cook'}
		print(content["name"]) # Spongebob
		print(content["age"]) # 30
		print(content["job"]) # cook
except FileNotFoundError:
	print(f"file '{file_path}' is missing")
except PermissionError:
	print(f"file '{file_path}' has no permission")


# -----------------

file_path = "./Input/input.csv"
print()
try:
	with open(file_path, "r") as file: # don't forget to put the 'r' in quotes: "r"
		content = csv.reader(file)
		for line in content:
			print(line)
except FileNotFoundError:
	print(f"file '{file_path}' is missing")
except PermissionError:
	print(f"file '{file_path}' has no permission")

# ['Name', 'Age', 'Job']
# ['Spongebob', '30', 'Cook']
# ['Patrick', '37', 'Unemployed']
# ['Sandy', '27', 'Scientist']