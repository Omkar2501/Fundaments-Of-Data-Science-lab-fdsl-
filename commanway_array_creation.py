import numpy as np

zeros_array = np.zeros((3,4))
print("Zeros Array:\n",zeros_array)

ones_array=np.ones((2,3))
print("Ones Array:\n",ones_array)

full_array=np.full((2,3),7)
print("Full Array:\n",full_array)

identity_array=np.eye(4)
print("Identity Array:\n",identity_array)

range_array=np.arange(0,10,2)
print("Range Array:\n",range_array)

lin_arr=np.linspace(0,1,5)
print("Linspace Array:\n",lin_arr)

rand_arr=np.random.rand(2,3)
print("Random Array:\n",rand_arr)
#[[0.96140805 0.14373775 0.4809121 ]
#[0.66283848 0.82450389 0.0676965 ]]

randit_arr=np.random.randint(1,10,(2,3))
print("Random Integer Array:\n",randit_arr)
#Random Integer Array:
# [[9 6 4]
# [6 9 9]]



