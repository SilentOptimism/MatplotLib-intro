# Numpy is very fast apparently vs default python
# Numpy is written in C++ or C
# An array object in numpy is ndarray
# Numpy is an opensource project

#importing the numpy library
import numpy

#importing numpy under the alias of np
import numpy as np



zeroDArray = np.array(41)
print(zeroDArray)
print(type(zeroDArray))
print(zeroDArray.ndim)

oneDArray = np.array([1,2,3,4])
print(oneDArray)
print(type(oneDArray))
print(oneDArray.ndim)

# An array of ndarrays
twoDArray = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(twoDArray)
print(type(twoDArray))
print(twoDArray.ndim)

# Why is ndmin != ndim ?????
fiveDArray = np.array([1,2,3,4,5], ndmin = 5)
print(fiveDArray)
print("Dimension count:", fiveDArray.ndim)

#prints the version
print(np.__version__)

print('Index 1, Element 2 oneDArray:', oneDArray[1])

# The new print method/old print method works
print('Row 1, Column 0, Element 1 twoDarray:', twoDArray[1][0])
print('Row 1, Column 0, Element 1 twoDarray:', twoDArray[1,0])

arr = np.array([1,2,3,4])

print(arr[2] + arr[3])

#ndarrays must be homogenous in shape
threeDArray = np.array([[[0,1],
                         [2,3],
                         [4,5],
                         [6,7]],
                        
                        [[8,9], 
                         [10,11], 
                         [12,13], 
                         [14,15]]])

print("Element:", threeDArray[0,0,0])

for slice in threeDArray:
    for row in slice :
        for element in row:
            print(element)

print()
print()
print()

#variables
x = 1
x = x + 2
print(x)

#strings
x = "abc"
y = "de"
z = x + y
print(z)

#functions
def f(x):
    y = x+2
    return y
f(5)

#if statements
x = 2
if x+1 == 3:
    print(x)

print ("next")
#loops
for i in range(1,100):
    if i%2 == 0:
        print(i)

    