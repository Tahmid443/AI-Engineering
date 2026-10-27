import numpy as np
'''
np.zeros() -> Array using zeros
'''
# np.zeros()
arr = np.zeros((2,3),dtype = np.int32)
print(arr)

# np.zeros_like()
arr1 = [[1,2,3],[4,5,6]]
arr2 = np.zeros_like(arr1) # copy of arr1 but all elements will 0
print(arr2)

"""
np.ones() -> Array using ones
"""

# np.ones()
arr = np.ones((3,4,3))
print(arr)

# np.ones_like()
arr1 = [[3,4,6],[4,6,3]]
arr2 = np.ones_like(arr1)
print(arr2) # copy of arr1 but replace all values with 1

"""
np.empty() -> empty array using random value
"""

# np.empty()
arr = np.empty((4,3))
print(arr)

# np.empty_like()
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.empty_like(arr1)
print(arr2) # it doesn't generate garbage value but randomize the arr1 elements

'''
np.full()
'''

# np.full()
arr = np.full((4,3),7)
print(arr)

arr = np.full((4,3),np.inf)
print(arr) # array with inf values

# np.full_like()
arr1 = np.array([1,2,3])
arr2 = np.full_like(arr1,3)
print(arr2)