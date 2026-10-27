import numpy as np 

# np.arange()
arr = np.arange(1,10,1) #(init val,final val(not included),step)
print(arr)
mt = arr.reshape(3,3) # we can reshape the array,The multiplication of the shapes should be equal to the number of elements in tha array
print(mt)

# np.linspace()
arr = np.linspace(0,4,6)
print(arr) # 0 to including 4, 6 values with same diff between
arr = np.linspace(0,4,6, endpoint=False) # 4 will not included (3.999999999)
print(arr) 

# np.logspace()
arr = np.logspace(0,4,6, base = 2) #default = 10 
print(arr) #(6 values between 2^0 -> 2^4) 0 -> 4:range of log values, base = 2, number of values = 6
