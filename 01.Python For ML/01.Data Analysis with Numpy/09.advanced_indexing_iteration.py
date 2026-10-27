import numpy as np 

# Integer Indecxing
lst = np.array([10,20,30,40])
values = lst[[0,3,1]] #0,3 and 1 index value
print(values)

# 2D Integer Indexing
arr2 = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr2[[0,1],[1,2]])

# Boolean Indexing
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr[arr>1]) # arr > 1 create boolean array which will choose value according to the condition

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
arr[arr>2] = 0
print(arr) # If value>2 then replace with 0


# Iterating over arrays
# we can use nd.nditer() to iterate through the multi dimensional array
arr3 = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
])

for i in np.nditer(arr3):
    print(i)