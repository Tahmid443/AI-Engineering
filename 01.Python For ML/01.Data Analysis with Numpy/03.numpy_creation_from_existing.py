import numpy as np
'''
List to numpy array
'''
# From list
list1 = [10,20,30,40,50]

arr = np.array(list1,dtype = np.int32)
print(arr)
print(arr.dtype)

# From mixed list
list2 = [10,True,'Tahmid']
arr = np.array(list2)
print(arr)

# From nested list
matrix = [[1,2,3],[4,5,6]]
arr = np.array(matrix)
print(arr)
print(arr.dtype)

'''
Tuple to numpy array
'''
# From tuple
tpl = (10,20,30)
arr = np.array(tpl)
print(arr)

'''
Set to numpy array
'''
# From set
st = {1,2,3}
arr = np.array(list(st))
print(arr)

'''
Dictionary to numpy array
'''
# From Dictionary
dc = {
    'a':10,
    'b':20,
    'c':30,
}
arr1 = np.array(list(dc.keys())) # array of dict keys
arr2 = np.array(list(dc.values())) # array of dict values
arr3 = np.array(list(dc.items())) # array of dict items(pair)
print(arr1)
print(arr2)
print(arr3)