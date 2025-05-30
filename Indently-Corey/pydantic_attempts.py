# YT link: https://www.youtube.com/watch?v=XIdQ6gO3Anc
# find there also Validator decorator to apply a customed validation on eny argument on your class (e.g. for initiation, for value toi be within range TBD)

# install the following packagess via 'uv add requirements.txt':
# "matplotlib>=3.10.3",
# "pandas>=2.2.3",
# "pydantic[email]>=2.11.5",


from pydantic import BaseModel, EmailStr, StrictStr, StrictInt, Field, validator



# basic
class User(BaseModel):
    name: StrictStr
    # name: str
    email: EmailStr
    account_id: StrictInt
    # account_id: int


try:
    user = {"name": "Shai", "email": "userphilips.com", "account_id": 12345}
    new_user = User(**user)
except Exception as e:
    print(e)
finally:
    user = {"name": "Shai", "email": "user@philips.com", "account_id": 12345}
    new_user = User(**user)
# 1 validation error for User email:
# value is not a valid email address: An email address must have an @-sign. [type=value_error, input_value='userphilips.com', input_type=str]



print()


# note that it can also catch multiple validation errors (if such introduced)
try:
    user = {"name": "Shai", "email": "user@philips.com", "account_id": "12345"}
    new_user = User(**user)
except Exception as e:
    print(e)
finally:
    user = {"name": "Shai", "email": "user@philips.com", "account_id": 12345}
    new_user = User(**user)
# 1 validation error for User account_id:
# Input should be a valid integer [type=int_type, input_value='12345', input_type=str]



print()




print(new_user) # auto repl that youdon't get with the basic class
# name='Shai' email='user@philips.com' account_id=12345


print()

class MyClass(BaseModel):
    install_component_version: str = Field(pattern=r"^[0-9]{2}\.[0-9]+\.[0-9]+$")

# my_class = MyClass(install_component_version="20.1984.70")

try:
    my_class = MyClass(install_component_version="2025/1984/70")
except Exception as e:
    print(e)
finally:
    my_class = MyClass(install_component_version="20.1984.70")
    # install_component_version = "20.1984.70"


print("\n", my_class.install_component_version)
# 2025.1984.70


# ==================================
# using customed validation (validator decorator)
# ==================================

print()

class Values(BaseModel):
    temperature: int
    humidity: int
    device: str

    @validator("temperature")
    def validate_temperature(cls, value):
        if not (-10 <= value <= 60):
            raise ValueError("Temperature must be between 0 and 100.")
        return value


    @validator("humidity")
    def validate_humidity(cls, value):
        if not (0 <= value <= 100):
            raise ValueError("Humidity must be between 0 and 100.")
        return value

reader1 = Values(temperature=25, humidity=50, device="sensor1")
# temperature=25 humidity=50 device='sensor1'

try:
    reader2 = Values(temperature=70, humidity=50, device="sensor2")
except Exception as e:
    print(e)
# Value error, Temperature must be between -10 and 70. [type=value_error, input_value=70, input_type=int]
# note that there's a bug in the debug printout


import inspect  # noqa: E402
from pprint import pprint  # noqa: E402
pprint(inspect.getmembers(Values, inspect.isfunction)) # list all functions in the class (thanks for using the pydantic 'BaseModel' decorator)
# [('__copy__', <function BaseModel.__copy__ at 0x0000025CE6074A40>),
#  ('__deepcopy__', <function BaseModel.__deepcopy__ at 0x0000025CE6074AE0>),
#  ('__delattr__', <function BaseModel.__delattr__ at 0x0000025CE6074D60>),
#  ('__eq__', <function BaseModel.__eq__ at 0x0000025CE6074FE0>),
#  ('__getattr__', <function BaseModel.__getattr__ at 0x0000025CE6074B80>),
#  ('__getstate__', <function BaseModel.__getstate__ at 0x0000025CE6074EA0>),
#  ('__init__', <function BaseModel.__init__ at 0x0000025CE6073D80>),
#  ('__iter__', <function BaseModel.__iter__ at 0x0000025CE6075080>),
#  ('__pretty__', <function Representation.__pretty__ at 0x0000025CE5E7E5C0>),
#  ('__replace__', <function BaseModel.__replace__ at 0x0000025CE6074E00>),
#  ('__repr__', <function BaseModel.__repr__ at 0x0000025CE6075120>),
#  ('__repr_args__', <function BaseModel.__repr_args__ at 0x0000025CE60751C0>),
#  ('__repr_name__',
#   <function Representation.__repr_name__ at 0x0000025CE5E7E3E0>),
#  ('__repr_recursion__',
#   <function Representation.__repr_recursion__ at 0x0000025CE5E7E480>),
#  ('__repr_str__', <function Representation.__repr_str__ at 0x0000025CE5E7E520>),
#  ('__rich_repr__',
#   <function Representation.__rich_repr__ at 0x0000025CE5E7E660>),
#  ('__setattr__', <function BaseModel.__setattr__ at 0x0000025CE6074C20>),
#  ('__setstate__', <function BaseModel.__setstate__ at 0x0000025CE6074F40>),
#  ('__str__', <function BaseModel.__str__ at 0x0000025CE6075260>),
#  ('_calculate_keys',
#   <function BaseModel._calculate_keys at 0x0000025CE6075DA0>),
#  ('_copy_and_set_values',
#   <function BaseModel._copy_and_set_values at 0x0000025CE6075C60>),
#  ('_iter', <function BaseModel._iter at 0x0000025CE6075BC0>),
#  ('_setattr_handler',
#   <function BaseModel._setattr_handler at 0x0000025CE6074CC0>),
#  ('copy', <function BaseModel.copy at 0x0000025CE60758A0>),
#  ('dict', <function BaseModel.dict at 0x0000025CE6075440>),
#  ('json', <function BaseModel.json at 0x0000025CE60754E0>),
#  ('model_copy', <function BaseModel.model_copy at 0x0000025CE6074180>),
#  ('model_dump', <function BaseModel.model_dump at 0x0000025CE6074220>),
#  ('model_dump_json',
#   <function BaseModel.model_dump_json at 0x0000025CE60742C0>),
#  ('model_post_init',
#   <function BaseModel.model_post_init at 0x0000025CE60744A0>)]





# =============================
# dataclass build-in alternative
# =============================


print()

from dataclasses import dataclass # not much data validation here!
# from dataclasses import dataclass, field

@dataclass
class DataClassUser:
    name: str
    email: str
    account_id: int


shai = DataClassUser(name='Shai', email="user@philips.com", account_id=12345)
print(shai)
# DataClassUser(name='Shai', email='user@philips.com', account_id=12345)