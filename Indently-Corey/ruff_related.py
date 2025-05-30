# in conjunction with the ruff section added to the pyproject.toml file

import pandas

def isEven(number): # here ruff suggest to replace w/ lower case for functions, e.g. is_even
    """Check if a number is even."""
    if number % 2 == 0:
        return True
    else: # here ruff suggest to dump the else since not neccessary when having return ("R", # Refactoring suggestions)
        return False





