# herein a profound example of utilizing the Enum class from the Python standard library.

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    def describe(self):
        return f"This color is {self.name.lower()}."


# Example usage
if __name__ == "__main__":
    color = Color.RED
    print(color)  # Output: Color.RED
    print(color.describe())  # Output: This color is red.
    
    # Iterating through the Enum members
    for c in Color:
        print(c, c.value)  # Output: Color.RED 1, Color.GREEN 2, Color.BLUE 3



# =====================================================================


# herein a profound example of utilizing the Enum basic class from the Python standard library.
from enum import Enum, auto
class Status(Enum):
    PENDING = auto() # behind the scenes is is 1
    APPROVED = auto() # behind the scenes is is 2
    REJECTED = auto()  # behind the scenes is is 3

    def is_final(self):
        return self in {Status.APPROVED, Status.REJECTED}


from enum import Flag, auto
class Permission(Flag):
    READ = auto() # behind the scenes is is 1 (2^0)
    WRITE = auto()  # behind the scenes is is 2 (2^1)
    EXECUTE = auto() # behind the scenes is is 4 (2^2) to allow combining with other flags
    DELETE = auto() # behind the scenes is is 8 (2^3) to allow combining with other flags


# Example usage
if __name__ == "__main__":
    # Combining permissions
    permissions = Permission.READ | Permission.WRITE # union of flags
    print(permissions)  # Output: Permission.READ|WRITE (<Permission.READ|WRITE: 3>)
    print(permissions.value) # Output: 3 (the sum of the values of the flags, 1 + 2 = 3)


    # Checking for specific permissions
    if Permission.READ in permissions: # like working with a set of values
        print("Read permission granted.")  # Output: Read permission granted.
    
    if Permission.EXECUTE not in permissions:
        print("Execute permission not granted.")  # Output: Execute permission not granted.
    
    # Iterating through the Flag members
    for perm in Permission:
        print(perm)  # Output: all supported permissions in the general class: Permission.READ, Permission.WRITE, etc.

    for perm in permissions:
        print(perm)  # Output: Permission.READ \n Permission.WRITE



# =====================================================================


# herein a profound example of utilizing the Enum Flag class from the Python standard library for combination of hw potential errors.
from enum import Flag, auto
class HardwareError(Flag):
    OVERHEAT = auto() # behind the scenes is is 1 (2^0)
    POWER_FAILURE = auto()  # behind the scenes is is 2 (2^1)
    MEMORY_LEAK = auto()    # behind the scenes is is 4 (2^2)
    DISK_FAILURE = auto()   # behind the scenes is is 8 (2^3)
    NETWORK_ISSUE = auto()  # behind the scenes is is 16 (2^4)

# Example usage
if __name__ == "__main__":
    # Combining hardware errors
    errors = HardwareError.OVERHEAT
    errors = errors | HardwareError.POWER_FAILURE
    errors |= HardwareError.NETWORK_ISSUE
    print(errors)  # Output: HardwareError.OVERHEAT|POWER_FAILURE|NETWORK_ISSUE

    # Checking for specific hardware errors
    if HardwareError.OVERHEAT in errors:
        print("Overheat detected.")  # Output: Overheat detected.
    
    if HardwareError.MEMORY_LEAK not in errors:
        print("No memory leak detected.")  # Output: No memory leak detected.
    
    # Iterating through the Flag members
    for error in HardwareError:
        print(error)  # Output (all class supported error): HardwareError.OVERHEAT, etc.

    print(errors.value) # Output: 19


    