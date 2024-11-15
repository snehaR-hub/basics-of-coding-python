'''1. Accessing Variables in Python
A variable in Python is simply a name that references a value. You access it by calling the variable name.'''

# Assign values to variables
x = 10
name = "Alice"

# Access the variables
print(x)      # Output: 10
print(name)   # Output: Alice

'''2. Accessing Elements in a List
A list is an ordered collection of items. You can access elements using an index (starting from 0).'''

# List of numbers
numbers = [10, 20, 30, 40, 50]

# Access elements by index
print(numbers[0])   # Output: 10 (first element)
print(numbers[2])   # Output: 30 (third element)

# Access last element
print(numbers[-1])  # Output: 50 (last element)

# Slicing the list
print(numbers[1:4]) # Output: [20, 30, 40] (elements from index 1 to 3)

'''3. Accessing Items in a Dictionary
A dictionary is a collection of key-value pairs. You access values by using their corresponding keys.'''

# Dictionary of user information
user = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing values by key
print(user["name"])  # Output: Alice
print(user["age"])   # Output: 30

# Checking if a key exists before accessing
if "city" in user:
    print(user["city"])  # Output: New York

'''4. Accessing Elements in a Tuple
A tuple is similar to a list but is immutable. You access elements in a tuple in the same way as a list using an index.'''

# Tuple of numbers
coordinates = (10, 20, 30)

# Access elements by index
print(coordinates[0])   # Output: 10
print(coordinates[2])   # Output: 30

'''5. Accessing Records in a Pandas DataFrame
In data analysis, you often use the pandas library to work with tabular data (like in spreadsheets or databases). A DataFrame is a 2D labeled data structure.'''

import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Access columns by name
print(df["Name"])  # Output: Alice, Bob, Charlie
print(df["Age"])   # Output: 25, 30, 35

# Access specific record (row) by index
print(df.iloc[1])  # Output: Bob's record (index 1)

# Access using conditions
print(df[df["Age"] > 30])  # Output: Charlie's record

'''6. Accessing Records in a Set
A set is an unordered collection of unique items. Since sets are unordered, you cannot access elements by index, but you can loop through them.'''

# Set of numbers
unique_numbers = {10, 20, 30, 40, 50}

# Access elements using a loop
for num in unique_numbers:
    print(num)

# Check if an element is in the set
print(30 in unique_numbers)  # Output: True

'''7. Accessing Attributes and Methods in a Class
In Object-Oriented Programming (OOP), objects of a class have attributes (variables) and methods (functions). You can access these using the dot (.) operator.'''

class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    def greet(self):   # Method
        return f"Hello, {self.name}!"

# Create an object of Person class
person1 = Person("Alice", 30)

# Access attributes
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30

# Access method
print(person1.greet())  # Output: Hello, Alice!

'''8. Accessing Items in a File (Reading File Records)
To access records or data stored in a file (such as a text file), you can open the file and read it line by line.'''

# Reading a file line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # Access each line in the file

'''9. Accessing Environment Variables
You can access environment variables using the os module.'''

import os

# Accessing an environment variable
home_directory = os.getenv("HOME")
print(home_directory)  # Output: Path to the home directory (depending on OS)

# If the environment variable doesn't exist
print(os.getenv("MY_VARIABLE", "Default Value"))  # Output: Default Value if MY_VARIABLE is not found

'''10. Accessing Command-Line Arguments
To access command-line arguments passed to a Python script, you can use the sys.argv list.'''

import sys

# Access command-line arguments
print(sys.argv)  # Prints the list of arguments
