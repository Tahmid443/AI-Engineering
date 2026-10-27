import numpy as np 

# np.diag() -> Diagonal matrix
diagonal_matrix = np.diag([1,2,3,4]) #Put this value diagonally and other values become 0
print(diagonal_matrix)

#np.eye() -> Create identity matrix
identity_matrix = np.eye(4) # Identity matrix of 4x4
print(identity_matrix)
 
identity_matrix = np.eye(3,4)
print(identity_matrix)

#np.eye(row,col,k) with k parameter
identity_matrix = np.eye(3,4,1) #1 step up
print(identity_matrix)
identity_matrix = np.eye(3,4,-1) #1 step down
print(identity_matrix)