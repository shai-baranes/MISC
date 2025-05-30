# info
# w/ dataclass you get auto init and easy class representation without having to define the __REPR__ & __STR__
# w/ dataclass you can also compare 2 exact items (==) and you'll get either True or False if they are instantiated equally

# ============================================
# in the old way
# ============================================



from dataclasses import dataclass, field

class Person:
    def __init__(self, name: str, age: int, iq: int = 100):
        self.name = name
        self.age = age
        self.iq = iq

    # if you want to compare instance with other instance w/o using dataclass
    def __eq__(self, other):
        return self.__dict__ == other.__dict__ #note: self.__dict__ is -> {'name': 'shai', 'age': 51, 'iq': 100}

    def __str__(self):
        return f"{self.name}: Age = {self.age}"



p1 = Person('shai', 51)
p2 = Person('shai', 51)
print(p1)
# <__main__.Person object at 0x00000292D3AC81D0> # if not impleenting the __str__(self) dunder method
# shai: Age = 51 # after implementing the __str__(self) dunder method

print(p1==p2)
# False  (only if you dont have the def __eq__() method)
print(p1 is p2)
# False (always)





# ============================================
# "dataclass" way
# ============================================
# note that 'pydantic' is a smart alternative to dataclass (refer to 'pydantic_attempts.py')

@dataclass
class Person:
    name: str
    age: int
    iq: int = 100
    # can_vote: bool = field(init=False) # it is not clear when using the 'field' attribute



# p1 = Person('John', 25)
p1 = Person('shai', 51)
p2 = Person('shai', 51)

print(p1)
# Person(name='shai', age=51, iq=100)

print(p1==p2)
# True
print(p1 is p2)
# False



@dataclass
class Person:
    name: str
    age: int
    iq: int = 100
    can_vote: bool = field(init=False)

    def __post_init__(self):
        # print('called __post_init__ method')
        self.can_vote = 18 <= self.age <= 70

p2 = Person('shai', 51)
print(p2)
# Person(name='shai', age=51, iq=100, can_vote=True)
print(p2.can_vote)
# True


# @dataclass(frozen=True, slots = True) # to freeze the instance values w/o been able to change it
@dataclass(frozen=True) # to freeze the instance values w/o been able to change it (immutable)
class Fruit:
    name: str
    calories: float = 10


my_fruit = Fruit("apple")
# >>> my_fruit.calories = 20
# >>> my_fruit.name = "orange"
# dataclasses.FrozenInstanceError: cannot assign to field 'name'
# dataclasses.FrozenInstanceError: cannot assign to field 'calories'






@dataclass
class Person:
    name: str
    age: int
    job: str = None
    friends: list[str] = None # note that you cannot apply default values in list without the use of default_factory. (TBD how?)
    # friends: list[str] = field(default_factory=list)  # this is the way to do this right (although there's no data validation)

    def __str__(self): # function override
        return f'{self.name} is {self.age} years old and works as a {self.job}. His friends are: {self.friends}'



## some data from the net
## same as below (w. or w/o type)
# json: dict = {
#     'name': 'Bob',
#     'age': 10,
#     'job': 'Salesman',
#     'friends': ['Mario', 'Luigi'],
# }

json = {
    'name': 'Bob',
    'age': 10,
    'job': 'Salesman',
    'friends': ['Mario', 'Luigi'],
}

bob = Person(**json)
# same as 
bob = Person(json['name'], json['age'], json['job'], json['friends'])

print(bob)
# Bob is 10 years old and works as a Salesman. His friends are: ['Mario', 'Luigi']
# note that upon executing "> bob", we still get: Person(name='Bob', age=10, job='Salesman', friends=['Mario', 'Luigi'])


bob2 = Person(**json)

print(bob == bob2) # thanks to the @dataclass
# True




# adding some knowhow from YT: https://www.youtube.com/watch?v=vBH6GRJ1REM (mCoding)


from pprint import pprint  # noqa: E402, I001
import inspect  # for inspecting the class members  # noqa: E402
from dataclasses import dataclass, asdict, astuple  # noqa: E402

@dataclass(frozen=True, slots=True, order=True)  # frozen=True makes it immutable, slots=True saves memory, order=True allows comparison based on the order of attributes
class Comment:
    id: int
    text: str
    # text: str = field(default="") # above is same as this
    replies: list[str] = field(default_factory=list, compare=False, repr=False)  # replies will not be considered in comparison; repr=False means that this field will not be included in the string representation of the class instance

comment = Comment(1, "I just subscribed!", ["Thanks!", "Welcome!"])
print(comment)
# Comment(id=1, text='I just subscribed!')

print(astuple(comment)) # (1, 'I just subscribed!', ['Thanks!', 'Welcome!'])
print(asdict(comment)) # {'id': 1, 'text': 'I just subscribed!', 'replies': ['Thanks!', 'Welcome!']}

comment2 = Comment(**asdict(comment))  # create a new instance from the existing one
comment2.replies.append("Great content!")  # modify the replies list in the new instance
comment2.replies
# ['Thanks!', 'Welcome!', 'Great content!'] # vs. ['Thanks!', 'Welcome!']

print(comment == comment2)  # True, thanks to 'compare = False'

pprint(inspect.getmembers(Comment, inspect.isfunction))  # list all functions in the class (thanks for using the dataclass decorator)
# [('__delattr__', <function Comment.__delattr__ at 0x0000024F8D701300>),
#  ('__eq__', <function Comment.__eq__ at 0x0000024F8D700F40>),
#  ('__ge__', <function Comment.__ge__ at 0x0000024F8D7011C0>), # from order = True
#  ('__getstate__', <function _dataclass_getstate at 0x0000024F8D6EDC60>), # from slots = True
#  ('__gt__', <function Comment.__gt__ at 0x0000024F8D701120>), # from order = True
#  ('__hash__', <function Comment.__hash__ at 0x0000024F8D7013A0>), # from frozen=True
#  ('__init__', <function Comment.__init__ at 0x0000024F8D700E00>),
#  ('__le__', <function Comment.__le__ at 0x0000024F8D701080>), # from order = True
#  ('__lt__', <function Comment.__lt__ at 0x0000024F8D700FE0>), # from order = True
#  ('__repr__', <function Comment.__repr__ at 0x0000024F8D700EA0>),
#  ('__setattr__', <function Comment.__setattr__ at 0x0000024F8D701260>),
#  ('__setstate__', <function _dataclass_setstate at 0x0000024F8D6EDD00>)] # from slots = True



