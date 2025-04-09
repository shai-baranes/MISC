import csv
# note that pandas has a great function to collect data from CSV files

my_ids = [] # both array and set would work here exactly the same way!
# my_ids = set() 

path = "./Input/LogFile_Noga.txt"
# path = "C:/assignment/LogFile.txt"
csv_file = open(path, 'r', newline='') # to avoid empty lines between rows
csv_content = csv.reader(csv_file)
lines = [line for line in csv_content]

for line in lines:
     if line[0].strip() not in my_ids:
        my_ids.append(line[0].strip())
        # my_ids.add(line[0].strip())
        print(line[0].strip() + " " + line[1].strip())






# ------------------

## 1st assignemnt:
# 2) Print the 3 first fields of each line - only first appearance of the first field - using the exact format as shown below:
# 52343 28-05-2017 15:01:54.158
# 52356 28-05-2017 15:01:54.731
# 52352 28-05-2017 15:01:54.771
# 52397 28-05-2017 15:01:55.065
# 52324 28-05-2017 15:01:55.226


## 2nd assignment: print the number of lines in text file

# with open(r"C:/assignment/LogFile.txt", 'r') as f:
#     for count, line in enumerate(f):
#         pass

# print('Total Lines', count + 1)

