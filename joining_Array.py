import numpy as np

#joining arays
a=np.array([1,2,3])
b=np.array([4,5,6])

joined=np.concatenate((a,b))
print("Joined Array:",joined)

stacked_v=np.vstack((a,b))
stacked_h=np.hstack((a,b))
print("vertically Stack:\n",stacked_v)
print("Horizontal stack:\n",stacked_h)


#vertically Stack:
# [[1 2 3]
# [4 5 6]]

#Horizontal stack:
# [1 2 3 4 5 6]

#Sorting Array
unsorted_array=np.array([6,3,9,0,2])
print("Unsorted Array:",unsorted_array)
print("Sorted Array:",np.sort(unsorted_array))

arr10=np.array([[1,2,3],[4,5,6]])
print("Shape:",arr10.shape)
print("Size:",arr10.size)
print("Reshaped :\n",arr10.reshape(3,2))