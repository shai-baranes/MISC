# info
# w/ dataclass you get auto init and easy class representation without having to define the __REPR__ & __STR__
# w/ dataclass you can also compare 2 exact items (==) and you'll get either True or False if they are instantiated equally
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
@dataclass(frozen=True) # to freeze the instance values w/o been able to change it
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
    friends: list[str] = None

    def __str__(self):
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
# Person(name='Bob', age=10, job='Salesman', friends=['Mario', 'Luigi'])

bob2 = Person(**json)

print(bob == bob2) # thanks to the @dataclass
# True
