import numpy as np 

# Indexing
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([
    [1,2,3],
    [4,5,6]
])
arr2[0][2] = 100
print(arr2)

# Slicing
# To get a subarray from an array we use slicing; arr[start:end:step]

arr1 = np.array([1,2,3,4,5])
arr1_mod = arr1[1:4]
print(arr1_mod)
print(arr1)

# 2D array slicing(arr[row_start:row_end,col_start:col_end])

arr2 = np.array([
    [1,2,3],
    [4,5,6]
])
row_0 = arr2[0:1,]
row_1 = arr2[1:,]
col_0 = arr2[:,0:1]
col_1 = arr2[:,1:2]
print(row_0)
print(row_1)
print(col_0)
print(col_1)

portion = arr2[:,0:2]
print(portion)