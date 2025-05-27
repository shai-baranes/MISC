# https://www.youtube.com/watch?v=-aKFBoZpiqA



# without "Context Manager":
f = open(r'../Input/input.txt', 'r')
print(f.read())
f.close()


f.closed
# True

# ==============
print() # for line seperation
# ==============


# known inplementation for the above using the "Context Manager":

with open(r'../Input/input.txt', 'r') as f:
    print(f.read())


f.closed
# True



# Context Manager using a Class (Alternative solution):
class Open_File:
    """our alternative to 'Open' context manager"""
    def __init__(self, filename, mode): # setup (like Constructor)
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback): # tear-down (like Destructor)
        self.file.close()



# ==============
print() # for line seperation
# ==============



with Open_File(r'../Input/input.txt', 'r') as f:
    print(f.read())




f.closed
# True




# another option using a function instead of using a class:

from contextlib import contextmanager  # noqa: E402

@contextmanager
def Open_File2(file, mode):
    f = open(file, mode) # Constructor/Setup
    yield f # 'return' when using class and 'yield' when using func.
    f.close() # Destructor/tear-down



# normally we should wrap the constructor & yield under 'try' and the tear-down under 'finally'
@contextmanager
def Open_File3(file, mode):
    try:
        f = open(file, mode) # Constructor/Setup
        yield f # 'return' when using class and 'yield' when using func.
    finally:
        f.close() # Destructor/tear-down




# ==============
print() # for line separation
# ==============


with Open_File2(r'../Input/input.txt', 'r') as f:
    print(f.read())




f.closed
# True



# another nice and practical example of using a context manager:


import os  # noqa: E402, F401
from contextlib import contextmanager  # noqa: E402

cwd = os.getcwd()
os.chdir(r'../Input')
print(f'{os.listdir()=}')
os.chdir(cwd)

cwd = os.getcwd()
os.chdir(r'../Output')
print(f'{os.listdir()=}')
os.chdir(cwd)


def get_files_list(path):
    try:
        cwd = os.getcwd()
        os.chdir(path)
        print(f'{os.listdir()=}')

        # f = open(file, mode) # Constructor/Setup
        # yield f # 'return' when using class and 'yield' when using func.
    finally:
        os.chdir(cwd)


get_files_list('../Input')
get_files_list('../Output')




@contextmanager
def change_dir(path):
    try:
        cwd = os.getcwd()
        os.chdir(path)
        yield # yield the position (to remain within the context)
    finally:
        os.chdir(cwd)

print("line seperation:")

with change_dir('../Input'):
    print(f'{os.listdir()=}')
# os.listdir()=['data.csv', 'input.csv', 'input.json', 'input.txt', 'LogFile_Noga.txt', 're_input_file.txt', 'ToDo_Noga.txt']



os.getcwd()
# C:\\Python_Rust_Removal\\MISC\\Indently-Corey



with change_dir('../Output'):
    print(f'{os.listdir()=}')
# os.listdir()=['modified_data.csv', 'modified_data_2.csv', 'output.json', 'output.txt', 'output1.csv', 'output2.csv', 'output_1.txt', 'output_2.txt']

os.getcwd()
# C:\\Python_Rust_Removal\\MISC\\Indently-Corey

