import numpy as np
arr1=np.random.randint(1,10,(3,3))
arr2=np.random.randint(1,10,(3,3))

print(f"The first matrix : \n{arr1}")
print(f"The second matrix : \n{arr2}")
matrix_sub=arr1-arr2
matrix_add=arr1+arr2

print(f"Matrix Subtraction of two matrices : \n{matrix_sub}")
print(f"Matrix Addition of two matrices : \n{matrix_add}")
