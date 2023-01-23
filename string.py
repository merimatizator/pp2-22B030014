print("Hello")
print('Hello')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! " #The strip() method removes any whitespace from the beginning or the end:
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"#The replace() method replaces a string with another string:
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)


age = 36
txt = "My name is John, I am " + age
print(txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")