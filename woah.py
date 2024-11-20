#importing
import math
print(math.sqrt(9))

import time
print(time.ctime())

#arrays
a = [1,2,3,4]
print(a)
a.append(8)
print(a)


print("\nThe old way of looping through arrays")
#looping through arrays via 2 ways
for i in range(len(a)):
    print (a[i], end = ", ")
print()

print("\nThe modern way of looping through arrays using there pointers")
for x in a:
    print(x, end = ", ")
print()

print("\nDictionary")
#dictionary
d = {'cat':'meow', 'dog':'bark',
     'bird':'chirp'}

print(d['cat'])
print(d['dog'])
d['dog'] = 'run'
print(d['dog'])

#if-else
x = 2 
if x == 1:
    print(5)
else:
    print(1)

print("\nNext")
#function composition
def f(x):
    return 2*x

def g(y):
    return 1+y

print(g(f(3)))
print(f(g(3)))

print("\nNext")
a = [1,2,3,4,5]
print(a)
a.pop()
print(a)