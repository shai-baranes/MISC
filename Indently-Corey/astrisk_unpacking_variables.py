# unpacking a Tuple!



people: tuple[str, ...] = ('firstPerson', 'secondPerson', 'Bob', 'Ben', 'second2lastPerson', 'lastPerson')
# people = ['firstPerson', 'secondPerson', 'Bob', 'Ben', 'second2lastPerson', 'lastPerson'] # both work

first, *_, last = people

print(f'{first=} {last=}')

# first='firstPerson' last='lastPerson'


first, second,  *_, near_last, last = people # it helps to mask all in between that are no so interesting
# first,  *middle, last = people


print(f'{first=} {second=} {near_last=} {last=}')
# first='firstPerson' second='secondPerson' near_last='second2lastPerson' last='lastPerson'



# note also that _ is a list (the data that we're not going to use - a throw away varaible):
print(f'{_=}')
# _=['Bob', 'Ben']




# ================================


# how to avoid exceptions upon reading from dictionary and to avoid rewriting values if key already in dict!

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5,}  # noqa: F821

for char in ["a", "b", "c", "d", "e","f"]:
    print(my_dict.get(char)) # we get 'None' for "f" instead of exception!


my_dict.setdefault("a")
# {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5,}

my_dict.setdefault("f")
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': None}

my_dict.setdefault("a", 20)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': None}

my_dict.setdefault("g", 20)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': None, 'g': 20}


def main() -> None:
    print(f"this is {my_dict.get("a")}")

