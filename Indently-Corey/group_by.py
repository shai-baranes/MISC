from itertools import groupby
# https://www.youtube.com/watch?v=2d1BIiX8Kfw

# we can use list/dict comprehension instead but this is more memory efficient (since it is iterable)

# ============================
# basics
# ============================



def group_by(iterable, key=None): # grouping function without utilizing the pandas module
    """
    Groups elements of an iterable by a specified key function.

    Args:
        iterable: An iterable to group.
        key: A function that extracts a key from each element.

    Returns:
        A dictionary where the keys are the results of the key function
        and the values are lists of elements that correspond to each key.
    """
    if key is None:
        key = lambda x: x

    grouped = {} # empty dictionary to hold grouped elements
    for k, g in groupby(sorted(iterable, key=key), key=key): # similar elements per key must be sorted first by same key (near eachouther) for the feature to work!
    # for k, g in groupby(iterable, key=key):
        grouped[k] = list(g)
    
    return grouped



# Example usage:
if __name__ == "__main__":
    data = [1, 2, 2, 3, 3, 3, 4]
    words = ['Cat', 'Dog', 'Elephant', 'Seal', 'Turtle', 'Owl', 'Orange', 'Ear', 'Sony', 'Tony']
    grouped_data = group_by(data)
    print(f"{grouped_data=}")  # Output: {1: [1], 2: [2, 2], 3: [3, 3, 3], 4: [4]}
    
    data_with_keys = [('apple', 'red'), ('banana', 'yellow'), ('cherry', 'red')]
    grouped_by_color = group_by(data_with_keys, key=lambda x: x[1])
    print(f"{grouped_by_color=}")  # Output: {'red': [('apple', 'red'), ('cherry', 'red')], 'yellow': [('banana', 'yellow')]}

    grouped_by_len = group_by(data_with_keys, key=lambda x: len(x[0]) + len(x[1]))
    print(f"{grouped_by_len=}")
    # grouped_data={1: [1], 2: [2, 2], 3: [3, 3, 3], 4: [4]}
    # grouped_by_color={'red': [('apple', 'red'), ('cherry', 'red')], 'yellow': [('banana', 'yellow')]}
    # grouped_by_len={8: [('apple', 'red')], 9: [('cherry', 'red')], 12: [('banana', 'yellow')]}

    print()

    grouped_by_tbd = group_by(words, key=lambda s: s[0].lower())
    print(f"{grouped_by_tbd=}")
    # grouped_by_tbd={'c': ['Cat'], 'd': ['Dog'], 'e': ['Elephant', 'Ear'], 'o': ['Owl', 'Orange'], 's': ['Seal', 'Sony'], 't': ['Turtle', 'Tony']}


    people = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 30, 'city': 'New York'},
        {'name': 'David', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Eve', 'age': 35, 'city': 'Chicago'}   
    ]

    from operator import itemgetter

    grouped_by_city = group_by(people, key=itemgetter('city'))
    print(f"{grouped_by_city=}")
    # grouped_by_city={'Chicago': [{'name': 'Eve', 'age': 35, 'city': 'Chicago'}], 'Los Angeles': [{'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}, {'name': 'David', 'age': 25, 'city': 'Los Angeles'}], 'New York': [{'name': 'Alice', 'age': 30, 'city': 'New York'}, {'name': 'Charlie', 'age': 30, 'city': 'New York'}]}
