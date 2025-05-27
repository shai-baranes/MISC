# working with the 'pathlib' library to handle paths and files in a more robust way
import os # working with strings (old-school)
from pathlib import Path # workin with objects (less prone to errors)
import atexit



# ==================================
# The very Basic
# ==================================


MY_ROOT1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # __file__ is this file that we're running
# 'C:\\Python_Rust_Removal\\MISC'


print(Path(__file__).resolve()) # note that you can use either 'resolve()' or 'absolute()' ? TBD interchangable?
# C:\Python_Rust_Removal\MISC\Indently-Corey\path_lib.py


MY_ROOT2 = Path(__file__).resolve().parent.parent # clear short and robust!
# C:/Python_Rust_Removal/MISC



# ==================================
# iterating through local files
# ==================================

# printing all the files under the current working directory (current cwd)
for item in Path().iterdir():
    print(item)

# astrisk_unpacking_variables.py
# at_exit_advanced.py
# at_exit_advanced_2.py
# at_exit_basic.py
# context_manager.py
# path_lib.py


# working with 'relative' paths
my_dir = Path("Directory_1")
# my_dir # Directory_1
# my_dir.resolve() --> WindowsPath('C:/Python_Rust_Removal/MISC/Indently-Corey/Directory_1')

my_dir.parent
# .    # current location -> meaning that it is relative location

my_file = Path("context_manager.py")
# my_file.resolve() --> WindowsPath('C:/Python_Rust_Removal/MISC/Indently-Corey/context_manager.py')


# =================================
# easy access to either file name or extention
# =================================


# grab the extenstion is much simpler here!
my_dir.suffix # no need to get name and split and index...
# .py

my_file.suffix
# ''


# getting the names without the extensions
my_dir.stem
# Directory_1

my_file.stem
# context_manager



# =======================================
# joining file names to paths
# =======================================


# joining new file to path
new_file = my_dir / "new_file.txt"
# Directory_1\new_file.txt


# using absolute path
new_file2 = Path(__file__).parent / "another_file.txt"
# C:\Python_Rust_Removal\MISC\Indently-Corey\another_file.txt

## note that these files doesn't need to exist in order to create the paths

new_file2.exists()
# False

old_file = Path(__file__).parent / "at_exit_basic.py"
# C:\Python_Rust_Removal\MISC\Indently-Corey\at_exit_basic.py

old_file.exists()
# True


# =========================================
# where the .resolve() comes in handy comparing to the .absolute() method
# =========================================

Path("..").absolute()
# C:\Python_Rust_Removal\MISC\Indently-Corey\..


Path("..").resolve() # resolving ".." such marks, although it is the same yet now more readable!
# C:\Python_Rust_Removal\MISC


# ======================================
# working with Home Directory
# ======================================


# introducing Home directory: ~,  to .resolve() works the same as if using .absolute()
Path("~/dotfiles").resolve()
# C:/Python_Rust_Removal/MISC/Indently-Corey/~/dotfiles


Path("~/dotfiles").expanduser()
# C:/Users/shaib/dotfiles   # now it is fully resolved


# if youstart from scratch and want to work with Home directory
Path.home()
# C:/Users/shaib

Path.home() / "dotfiles"
# C:/Users/shaib/dotfiles





# ===========================================================
# searching for files names containing "subtext" or files of certain types (either recuresively or not)
# ===========================================================


my_path = Path.home() / "OneDrive" / "Documents"

# advanced searching in path
for item in my_path.glob("*reg*"):
    print(item)

# C:\Users\shaib\OneDrive\Documents\regexp_trials.py
# C:\Users\shaib\OneDrive\Documents\Regular Expression

print()


# search for files where filenames contain a subtext
for item in my_path.rglob("*reg*"): # 'rglob' for recursive search!
# for p in my_path.rglob("*reg*", case_sensitive=True): # not working for windows?
    print(item)

# C:\Users\shaib\OneDrive\Documents\regexp_trials.py
# C:\Users\shaib\OneDrive\Documents\Regular Expression
# C:\Users\shaib\OneDrive\Documents\python_attempts\regular_expression.py   


print()

# we can also search for files with specific extension (either recursively or non recuresively)
for item in my_path.glob("*.txt"): # 'rglob' for recursive search!
    print(item)

# C:\Users\shaib\OneDrive\Documents\Elbit_interview_prep.txt
# C:\Users\shaib\OneDrive\Documents\EPD_info.txt
# C:\Users\shaib\OneDrive\Documents\Hyuvim_Shonim.txt
# C:\Users\shaib\OneDrive\Documents\info.txt
# C:\Users\shaib\OneDrive\Documents\MSD_Nethania potential interview.txt
# C:\Users\shaib\OneDrive\Documents\nice.txt
# C:\Users\shaib\OneDrive\Documents\noga_info.txt
# C:\Users\shaib\OneDrive\Documents\Poultry_for_interview.txt
# C:\Users\shaib\OneDrive\Documents\prague_expenses.txt
# C:\Users\shaib\OneDrive\Documents\pycharm_info.txt
# C:\Users\shaib\OneDrive\Documents\SSH turorial.txt
# C:\Users\shaib\OneDrive\Documents\temp.txt
# C:\Users\shaib\OneDrive\Documents\temp_info.txt

print()


my_file = my_path / "temp_info.txt"

# this is the cat or echo usage from within python
with my_file.open() as f:
# with open(my_file) as f:  # equivalent to above (with or without the mode = "r" attribute)
    print(f.read())

## file content
# C:\Users\shaib\AppData\Roaming\Sublime Text\Packages\User\SublimeLinter.sublime-settings

# renamed to 

# C:\Users\shaib\AppData\Roaming\Sublime Text\Packages\User\SublimeLinter.sublime-settings.old


# ========================================================
# use the Path lib to easily create and remove directories
# ========================================================

p = Path("TempDir") # relative to current location

p.resolve()
# C:\Python_Rust_Removal\MISC\Indently-Corey\TempDir



p.mkdir() # creates this new directory locally

p.rmdir() # removes this new directory from locally (this removes only empty directories)


# if I want to create a chain of non-existing directories (directory which its parent is not existing yet)
p = Path("TempDir/Subdir") # relative to current location
p.mkdir(parents=True) # must add the parents attribute since we're dealing with linked non-existing directories


Path(p / "TempFile.txt").touch()
# Path("TempDir/Subdir/TempFile.txt").touch() # same as above


Path(p / "TempFile.txt").rename(p / "temp_file.txt")
# Path("TempDir/Subdir/TempFile.txt").rename("TempDir/Subdir/temp_file.txt") # same as above


import pdb; pdb.set_trace()  # breakpoint 41ea5149 //



# note that it is called only when running the script outside the IDE!
@atexit.register # first decorated function is the last to run upon exit
def terminate() -> None:
    
    # file removal
    Path(p / "temp_file.txt").unlink()  # removes the file
    # Path("TempDir/Subdir/temp_file.txt").unlink()  # same as above

    # directory removal
    p.rmdir()  # removes the empty directory

    print(p)
    # TempDir\Subdir

    p.parent.rmdir()  # removes the next empty directory ('TempDir')



# =========================================================


