import numpy as np

# data type
arr = np.array([1,2,3])
print(arr.dtype) #int64

arr = np.array([1.5,2.4,3.2])
print(arr.dtype) #float64

# Upcasting
arr = np.array([1, 2, 3.7])
print(arr.dtype) #float64

arr = np.array([1,2,3.2,'hello'])
print(arr.dtype) #<U32 [U -> Unicode String] (number -> string)

# Mixed data
arr = np.array([1,4.5,True,'Tahmid'])
print(arr.dtype) #<U32 (because of string)

'''
Data type change using astype()
'''
arr = np.array([1,2,3,5.8]) # float64
arr2 = arr.astype(np.int32) # int32
print(arr.dtype) # float64
print(arr2.dtype) # int32 (copy of arr)

# It will show error if you give wrong type
arr = np.array(
    [1, 2, 3.4, "hello"], dtype=np.int64
)  # ValueError: invalid literal for int() with base 10: 'hello'
