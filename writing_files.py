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
		file.write(txt_data) # we need to move to next line (written entirely in one chunk)
		print(f"txt file '{file1_path}' was created")
except FileExistsError:
	print(f"file: {file1_path.split('/')[-1]} already exists!")




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



file_path = "./Output/output1.csv"
file_path2 = "./Output/output2.csv"


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



# as if each time we're geeting nerw input by the user
# **note that the header is created only once!**

#note that the params can be reordered as long as the writerow knows the order of the params in the csv file
occupation, name, age,  = "Cook", "Spongebob", 30

# another option (if headers are not part of original content):
with open(file_path2, "a", newline="") as file: # adding argument "newline" to prevent empty row per row of data
	writer = csv.writer(file)
	writer.writerow([name, age, occupation])

name, age, occupation = "Patrick", 37, "Unemployed"

with open(file_path2, "a", newline="") as file: # adding argument "newline" to prevent empty row per row of data
	writer = csv.writer(file)
	writer.writerow([name, age, occupation])

age, name, occupation = 27, "Sandy", "Scientist"

with open(file_path2, "a", newline="") as file: # adding argument "newline" to prevent empty row per row of data
	writer = csv.writer(file)
	writer.writerow([name, age, occupation])


# and another robust way to do it (less prone to errors)

line_1 = {'name': 'Spongebob_2', 'age': '30_2', 'occupation': 'Cook_2'}
line_2 = {'name': 'Patrick_2', 'age': '37_2', 'occupation': 'Unemployed_2'}
line_3 = {'name': 'Sandy_2', 'age': '27_2', 'occupation': 'Scientist_2'}

# another option (if headers are not part of original content):
with open(file_path2, "a", newline="") as file: # adding argument "newline" to prevent empty row per row of data
	writer = csv.DictWriter(file, fieldnames=["name", "age", "occupation"]) # the order must be kept here
	writer.writerow(line_1)

with open(file_path2, "a", newline="") as file: # adding argument "newline" to prevent empty row per row of data
	writer = csv.DictWriter(file, fieldnames=["name", "age", "occupation"])
	writer.writerow(line_2)


with open(file_path2, "a", newline="") as file: # adding argument "newline" to prevent empty row per row of data
	writer = csv.DictWriter(file, fieldnames=["name", "age", "occupation"])
	writer.writerow(line_3)



name, age, occupation = "Patrick", 37, "Unemployed"

with open(file_path2, "a", newline="") as file: # adding argument "newline" to prevent empty row per row of data
	writer = csv.writer(file)
	writer.writerow([name, age, occupation])

age, name, occupation = 27, "Sandy", "Scientist"

with open(file_path2, "a", newline="") as file: # adding argument "newline" to prevent empty row per row of data
	writer = csv.writer(file)
	writer.writerow([name, age, occupation])






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

# I like pizza!
# It's really good!

# there's also an option to read it line by line instead of in one chunk:
print()

try:
	with open(file_path, "r") as file: # don't forget to put the 'r' in quotes: "r"
		lines = file.readlines() # lines are stored in a list of lines (we could replace it with: "for line in file:	print(line.rstrip())")
		for line in lines:
			print(line.rstrip())
except FileNotFoundError:
	print(f"file '{file_path}' is missing")
except PermissionError:
	print(f"file '{file_path}' has no permission")


# I like pizza!
# It's really good!

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


# # say we didn't have the csv library
# with open(file_path) as file: # 'r' by default
# 	for line in file:

with open(file_path) as file:
	for line in file:
		print(line.rstrip().split(","))

# ['Name', 'Age', 'Job']
# ['Spongebob', '30', 'Cook']
# ['Patrick', '37', 'Unemployed']
# ['Sandy', '27', 'Scientist']



# with open(file_path) as file:
# 	for line in file:
# 		name, age, job = line.rstrip().split(",") # unpacking the variables from the CSV file
# 		if name == 'name': # if header
# 			continue
# 		else:

figures = []

with open(file_path) as file: # for simplicity, I may skip the try/except wrapping
	for i, line in enumerate(file):
		if i ==0:
			continue
		else:
			name, age, job = line.rstrip().split(",") # unpacking the variables from the CSV file
			figures.append(f"{name} is {age} days old, occupation: {job}")

# ['Spongebob is 30 days old, occupation = Cook', 'Patrick is 37 days old, occupation = Unemployed', 'Sandy is 27 days old, occupation = Scientist']

print()

figures = [] # note that dict {} jas no attribute such as 'append'
#applyting the CSV into dictionary (still w/o relying oin the CSV lib)
with open(file_path) as file:
	for line in file:
		name, age, job = line.rstrip().split(",") # unpacking the variables from the CSV file
		if name == "Name":
			continue		
		figure = {}
		figure['Name'] = name
		figure['Age'] = age
		figure['Job'] = job
		figures.append(figure)

for figure in figures:
	print(f"Name = {figure['Name']}, Age = {figure['Age']}, Job = {figure['Job']}, ")

# figures = [{'Name': 'Spongebob', 'Age': '30', 'Job': 'Cook'}, {'Name': 'Patrick', 'Age': '37', 'Job': 'Unemployed'}, {'Name': 'Sandy', 'Age': '27', 'Job': 'Scientist'}]

print()

# let's print the list of dictionaries in a sorted way:
for figure in sorted(figures, key=lambda figure: figure['Age'], reverse = True): # note that the name of the argument is not important!
	print(figure)



#another option using function

def set_age(item):
	return item['Age']



for figure in sorted(figures, key=set_age):
	print(figure)



# the csv reader can handle lines of 3 params, as: ['Patrick', '37', 'Unemployed, but soon to be'] (note for the 3 ',' instead of 2 deviders)
try:
	with open(file_path, "r") as file: # don't forget to put the 'r' in quotes: "r"
		content = csv.reader(file) # the convention is calling it "reader" instead of "content"
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


print("temp")

figures = [] # to be list of dicts
# eventually: [{'Name': 'Spongebob', 'Age': '30', 'Job': 'Cook'}, {'Name': 'Patrick', 'Age': '37', 'Job': 'Unemployed'}, {'Name': 'Sandy', 'Age': '27', 'Job': 'Scientist'}]

# let's make it more robust using the csv lib power! (case where you must have context: column names!)
with open(file_path) as file: # don't forget to put the 'r' in quotes: "r"
	reader = csv.DictReader(file)
	for line in reader:
		figures.append(line)
		# figures.append({"Name": line["Name"], "Age": line["Age"], "Job": line["Job"]})



# now taking the list and putting it into the file using the power of csv lib:





# # temp:
# figures = [] # to be list of dicts
# file_path = "./Output/output2.csv"
# with open(file_path) as file: # don't forget to put the 'r' in quotes: "r"
# 	reader = csv.DictReader(file)
# 	for line in reader:
# 		figures.append(line)