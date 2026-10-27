import numpy as np 

# np.random.rand() -> from 0 to 1
arr = np.random.rand(2,3) # random value from 0 to 1 in array of 2 rows and 3 cols
print(arr)

# np.random.randint() -> we can define the range(int)
arr = np.random.randint(1,10,(2,3))
print(arr) #random values from 1-9 with 2 rows and 3 cols

# np.random.uniform() -> we can define the range(float)
arr = np.random.uniform(50,100,(3,3))
print(arr)