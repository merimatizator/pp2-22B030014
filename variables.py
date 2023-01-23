x = 5
y = "John"
print (x)
print (y)

x = 4
x = "Sally"
print (x)

x = str(3) # x will be '3'
x = int(3) # y will be 3
x = float(3) # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
x = 'John'

a = 4
A = "Sally"
print(a)
print(A)

myVariableName = "John" #camel case
MyVariableName = "John" #pascal case
my_variable_name = "John" #snake case

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"] #Unpack a Collection
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

