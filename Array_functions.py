import numpy as np

sample=np.array([[1,2,3],[4,5,6]])
print("Sample Array:\n",sample)

print("Shape:",sample.shape)  # (rows, columns)
#Shape: (2, 3)

print("Dimension:",sample.ndim) # number of axes
#Dimension: 2

print("Size",sample.size)  # total elements
#Size 6

print("Data Type:",sample.dtype) # data type of elements
#Data Type: int64

print("Reshape (3x2):",sample.reshape(3,2)) # Reshaping arrays
#Reshape (3x2): [[1 2]
# [3 4]
# [5 6]]


print("Flattened:",sample.flatten()) # Flattening to 1D
#Flattened: [1 2 3 4 5 6]

print("Transpose:\n",sample.T)# Transpose (swap rows and columns)
#\Transpose:
# [[1 4]
# [2 5]
# [3 6]]