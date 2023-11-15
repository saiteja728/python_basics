import numpy as np
OneDarray = np.array([10,11,12])
print("one dimensional array:",OneDarray)
TwoDarray = np.array([[10,11,12],[20,21,22]])
TwoDarray2 = np.array([[33,34,35],[20,88,22]])
resultArray = TwoDarray+TwoDarray2

print("------------1D arrays----------------")
print("addition of 2-D arrays:\n",resultArray)
print("one dimensional array\n:",OneDarray)
print("1d array of size:\n",OneDarray.size)
print("1d array of shape:\n",OneDarray.shape)

print("----------2d arrays------------")

print("2d dimensional array\n:",resultArray)
print("2d array of size:\n",resultArray.size)
print("2d array of shape:\n",resultArray.shape)
print('original result of 2d elements:\n',resultArray)
print("reverse of 2d elements:\n",resultArray[::-1])
print("original size of elements is:\n",TwoDarray)
print("squre the elements in 2d array is:\n",TwoDarray**2)

print("---------sum,product,division,modules,transpose-----------")
print("original size of elements is:\n",TwoDarray)
print("using sum() method we get all elements sum in array:/n",TwoDarray.sum())
print("using sum() method we get all row-wise elements sum in array:/n",TwoDarray.sum(axis=1))
print("using product() method we get all elements product in array:/n",TwoDarray.prod())
print("squre the elements in 2d array transpose is:\n",TwoDarray.transpose)
print("original size of elements reshape is:\n",TwoDarray.reshape(3,2))