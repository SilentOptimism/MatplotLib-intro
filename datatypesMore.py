#Data types: string, float, bool, NONE
s = "abc"
f = 1.0
b = True
n = None

#data casting
f = float("1")
s = str(1)

#this won't work as strings are immutable
s = "yello"
# s[0] = "D" #NO WORKY STRINGS ARE IMMUTABLE

#tuples
x = (1,2,3) # A tuple
y = [1,2,3] # A list
y[0] = 0
# x[0] = 0 #NO WORKY TUPLES ARE IMMUTABLE

#sets
s = set([1,2,3])
s.add(4)
print(s)
s.add(3) # This does nothing as sets can't have copies
print(s)