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


