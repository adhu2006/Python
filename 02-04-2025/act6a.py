import numpy as np
arr1=np.random.randint(1,20,(3,3))
mean=arr1.mean()
print(f"The array is : \n{arr1}")
print(f"The mean of the array is : {mean}")

#code to replace all elements less than 10 with 0
for i in range(3):
    for j in range(3):
        if arr1[i][j]<10:
            arr1[i][j]=0
print(f"Modified array : \n{arr1}")
