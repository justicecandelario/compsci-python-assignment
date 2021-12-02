import random 
import string 

# Create a comment with your name
#Justice Candelario

# Create a string called 'name' which stores your name
name = 'Justice Candelario'

# Print the 'name' variable
print(name)

# Create a variable storing an integer
var1 = 4

# Create a variable storing a floating point number
var2= 9.60

# This line creates a string of 1000000 random letters
rs = ''.join(random.choices(string.ascii_lowercase, k=1000001))
# Print whether your first name (lowercase) appears in the string
if 'justice' in rs:
  print("yes")
else:
  print("no")

# Print the first letter, last letter, and middle letter
print(rs[0], rs[-1], rs[len(rs)//2])

# This line creates a string of some random words
rw = ''.join(random.choices(list(string.ascii_lowercase) + [' '], k=1000))
# Print the number of words (a word being characters surrounded by spaces)
print(len(rw.split()))

# This is a string to be formatted
sentence = '{greeting}, my name is {name}'
# Print the sentence formatted with your choice of greeting and your name
print('Hello, my name is Justice Candelario')

# Create a variable storing a tuple of your three favorite numbers
favnumber = (3, 4, 8) 

# Assign those three numbers to variables 'a', 'b', and 'c' in one line
a, b, c = (3, 4, 8)

# Create a variable storing None
var = None

# Create a variable, lst, storing a list of the numbers 0-1000 (inclusive)
lst = []
for i in range(0, 1001):
  lst.append(i)

# Print the sum and average of the list
print(sum(lst))
print(sum(lst)/len(lst))

# Create a variable, ascii_low, storing a **set** of all lowercase ascii characters
ascii_low = []
for ch in string.ascii_lowercase:
  ascii_low.append(ch)
ascii_low = set(ascii_low)

# Create a varaible, ascii_all, storing a **set** of all ascii characters
ascii_all = []
for ch in string.ascii_letters:
  ascii_all.append(ch)
ascii_all = set(ascii_all)

# Create a variable, ascii_hi, storing the set different between ascii_all and
# ascii_low, i.e. (ascii_all - ascii_low)
ascii_hi = ascii_all - ascii_low

# Create a dictionary with one key, your first name that maps to one value,
# your last name
namedictionary = {}
namedictionary['Justice'] = 'Candelario'

# Alter the dictionary to make your last name all caps
namedictionary['Justice'] = namedictionary['Justice'].upper()

# Here is a nested structure
d = {'hello': [[{'cory': 'nezin'}, {'CORY': ['N', 'E', 'Z', 'I', 'N']}]]}
# Change the 'Z' from the list ['N', 'E', 'Z', 'I', 'N'] inside to a 'z'
((((d['hello'])[0])[1])['CORY'])[2] = ((((d['hello'])[0])[1])['CORY'])[2].lower()

# Use a for loop to print numbers 1 through 10 (inclusive)
for number in range(1, 11):
  print(number)

# Use a for loop to create a list of the first 10 cubes (0 through 9, cubed)
cube = []
for k in range(0, 10):
  cube.append(k**3)

# Now use a list comprehension to do the same
j = [(n**3) for n in range(0, 10)]

# Write a function 'unique' which takes a list and checks if each element is
# unique, meaning there are no duplicates inside the list.
def unique(my_list):
  counts = {}
  for element in my_list:
    counts[element] = 0
  for element in my_list:
    counts[element] = counts[element]+1
  for key in counts.key():
    if counts[key]>1:
      return False
  return True
