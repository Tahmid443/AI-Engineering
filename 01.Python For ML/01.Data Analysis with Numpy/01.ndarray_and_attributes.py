# Importing numpy
import numpy as np

# 1D Array
arr1 = np.array([1,2,3,4,5])

# 2D Array
arr2 = np.array([[1,2,3],[4,5,6]])

# 3D Array
arr3 = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]],
    [[13,14,15],[16,17,18]]
])

'''
Array Attributes
'''
# ndim (Dimension of array)
print(arr1.ndim) #1
print(arr2.ndim) #2
print(arr3.ndim) #3

# shape (element no(1D)/row,col(Multi))
print(arr1.shape) #5
print(arr2.shape) #(2,3)
print(arr3.shape) #(3,2,3)

# size (total element no)
print(arr1.size) #5
print(arr2.size) #6
print(arr3.size) #18

# dtype
print(arr1.dtype)