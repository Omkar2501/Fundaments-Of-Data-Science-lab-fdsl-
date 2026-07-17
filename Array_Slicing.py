import numpy as np

arr=np.array([10,20,30,40,50,60])

print("Full Array:",arr)
print("First element:",arr[0])
print("Last element:",arr[-1])
print("Element from index 1 to 3:",arr[1:4])
print("Every second element:",arr[::2])
print("Reversed Array:",arr[::-1])


matrix = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

print("Matrix:\n", matrix)
print("Element at row 1, col 2:", matrix[1, 2])
print("First row:", matrix[0, :])
print("First column:", matrix[:, 0])
print("Sub-matrix (rows 0-1, cols 1-2):\n", matrix[0:2, 1:3])
