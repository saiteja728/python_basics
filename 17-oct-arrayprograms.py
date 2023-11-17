import numpy as np

# Creating a zero-dimensional array
ZDArray = np.array(10)
print("the dimension of array:", ZDArray.ndim)
print("zero dimension array shape is:", ZDArray.shape)

# Creating a range array from 1 to 9
RangeArray = np.arange(1, 10)
print("range of elements are:", RangeArray)
print("range of elements of shape:", RangeArray.shape)
print("range of elements size are:", RangeArray.size)

# Creating a random range array with floating-point numbers from 1 to 9
RandomRangeArray = np.arange(1, 10, dtype=float)
print("range of random elements of shape:", RandomRangeArray.shape)
print("range of random elements size are:", RandomRangeArray.size)

# Creating a random array of shape (1, 10)
RandomArray = np.random.random((1, 10))
print("shape of random array:", RandomArray.shape)
print("size of random array:", RandomArray.size)

# Creating a zero array with shape (5, 2, 3, 4) and type float
zeroArray = np.zeros((5, 2, 3, 4), dtype=float)
print("zero array shape:", zeroArray.shape)
print("zero array:\n", zeroArray.ndim)

print("savetxt, loadtxt, zeroarray, onearray")
 