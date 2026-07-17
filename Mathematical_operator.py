import numpy as np

x=np.array([10,20,30,40])
y=np.array([1,2,3,4])

print("Addition:",x+y)
print("Subtraction:",x-y)
print("Multiplication:",x*y)
print("Division:",x/y)
print("Power:",x**2)

data=np.array([2,4,6,8,9,10,12,14])

print("Mean:",np.mean(data))
print("Sum:",np.sum(data))
print("Satandard deviation:",np.std(data))
print("Variance:",np.var(data))
print("minimum:",np.min(data))
print("maximun:",np.max(data))

# Universal functions work element-wise
nums=np.array([1,4,9,16])
print("Square root:",np.sqrt(nums))
print("Exponential:",np.exp(nums))
print("Logarithm:",np.log(nums))
print("Sine:",np.sin(nums))


# Matrix operations
m1=np.array([[1,2],[3,4]])
m2=np.array([[5,6],[7,8]])

print("Element-wise multiplication:\n",m1*m2)
print("Matrix multiplication:\n",np.dot(m1,m2))
print("Matrix multiplication (matul):\n",np.matmul(m1,m2))