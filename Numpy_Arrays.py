# NumPy arrays
# https://www.youtube.com/watch?v=lLRBYKwP8GQ

import numpy as np

my_array = np.arange(8)
# array([0, 1, 2, 3, 4, 5, 6, 7])
my_array = np.arange(1,8)
# array([1, 2, 3, 4, 5, 6, 7])
my_array = np.arange(1,8,2)
# array([1, 3, 5, 7])
my_array = np.arange(1,8,0.5) # we cannot get float by using range() -> range(1,8,0.5) => Exception!!!
# array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5. , 5.5, 6. , 6.5, 7. , 7.5])



# converting a list into numpy array: <class 'numpy.ndarray'>
# much better in memory efficiency! size can be huge
print(np.array([1,2,3]))
# [1 2 3]

from_list = np.array([1,2,3])
print(type(from_list))
# <class 'numpy.ndarray'>

print(type(from_list[0]))
# <class 'numpy.int32'>


from_list = np.array([1,2,3], dtype=np.int8) # saving much more space!
print(type(from_list[0]))
# <class 'numpy.int8'>


from_list = np.array([[1,2,3], [4,5,6]], dtype=np.int8) # saving much more space!
print(from_list)
# [[1 2 3]
#  [4 5 6]]

# print(f'{text:.^50}')





array_2d = np.array((np.arange(0,8,2), np.arange(1,8,2)), dtype=np.int8) # saving much more space!
print(array_2d)
# [[0 2 4 6]
#  [1 3 5 7]]

print(array_2d.shape)
# (2, 4)


array_2d = array_2d.reshape((4,2))
print(array_2d)
# array([[0, 2],
#        [4, 6],
#        [1, 3],
#        [5, 7]], dtype=int8)

print(array_2d.shape)
# (4, 2)


array_2d = array_2d.reshape(8)
print(array_2d)
# [0 2 4 6 1 3 5 7]


# empty arrays
empty_array = np.zeros((2,2))
# [[0. 0.]
#  [0. 0.]]

empty_array = np.ones((2,2))
# [[1. 1.]
#  [1. 1.]]

eye_array = np.eye(3) # Matrix of diagonal one (matrizat yehida)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

eye_array[eye_array == 0] = 2 # filling all the zero values with 2
# [[1. 2. 2.]
#  [2. 1. 2.]
#  [2. 2. 1.]]

eye_array[eye_array < 2] = 9
# [[9. 2. 2.]
#  [2. 9. 2.]
#  [2. 2. 9.]]


eye_array[0] = 3 # 1st row
# [[3. 3. 3.]
#  [2. 9. 2.]
#  [2. 2. 9.]]


eye_array[:,0] = 3 # 1st column
# [[3. 3. 3.]
#  [3. 9. 2.]
#  [3. 2. 9.]]


# sort arrays:

new_array = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1])
new_array = new_array.reshape(3,3)
# [[9 8 7]
#  [6 5 4]
#  [3 2 1]]


#by default it is sorting by rows
sorted_array = np.sort(new_array)
# [[7 8 9]
#  [4 5 6]
#  [1 2 3]]

sorted_array = np.sort(sorted_array, axis=0) # 0 indicates columns why -1 indicates rows
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

