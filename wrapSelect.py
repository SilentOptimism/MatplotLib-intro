#and/or
x = 5
y = 3
if x > 2 and y < 9:
    print("YIPPEE")

if x > 2 or y > 10:
    print("Either or YIPPEE")
    
#bring code to next line the (\) tells python to ignore this line break
# () {} , are Prefered as they do the same thing but cleaner and safer
# using backslashes is kind of a hacky way of doing things and should be avoided
# Due to backslashes being sensative to whitespace only use them under certain circumstances
long_variable_name = 5
if (long_variable_name + 12 < long_variable_name +1) <\
    (long_variable_name+5) < 4:
    print(5)

#string indexing
s = "how are you"
print (s[5])

#get first and last element from string or array
a = [2,4,6,8]
print(a[-1])
print(a[-2])
print(a[0])

#change directory and get current directory
import os
print(os.getcwd()) #Returns a string containing our current directory
print(os.getcwd()[17:]) #getting a slice of our array

# use the chdir function to change the directory
os.chdir('/an actually valid directory')
