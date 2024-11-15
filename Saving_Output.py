'''1. Saving Output to a Text File
You can use Python's built-in open() function to write data to a text file.'''

# Open a file in write mode ('w'), or append mode ('a')
with open("output.txt", "w") as file:
    file.write("Hello, this is a saved output.\n")
    file.write("This is the second line of output.")

'''2. Saving Output to a CSV File
The csv module can be used to save data in CSV format.'''

import csv

# Data to be saved
data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]

# Save to CSV
with open("output.csv", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    
'''3. Saving Output to a JSON File
To save data in JSON format, use the json module.'''

import json
# Data to be saved
data = {"name": "Alice", "age": 30, "city": "New York"}

# Save to JSON file
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)

'''4. Saving Output to an Excel File
Use the pandas library to save data as an Excel file.'''

import pandas as pd

# Data to be saved
data = {"Name": ["Alice", "Bob"], "Age": [30, 25]}
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("output.xlsx", index=False)


'''5. Saving Output to a Pickle File (Serialized Object)
You can serialize Python objects (e.g., lists, dictionaries) into a binary format using pickle.'''

import pickle

# Data to be saved
data = {"name": "Alice", "age": 30}

# Save to pickle file
with open("output.pkl", "wb") as file:
    pickle.dump(data, file)

'''6. Saving Output to a Log File
For logging purposes, you can use the built-in logging module to save logs to a file.'''

import logging

# Configure logging to file
logging.basicConfig(filename="output.log", level=logging.DEBUG)

# Save output to log
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.error("This is an error message.")

'''7. Redirecting Print Output to a File
If you want to save everything printed to the console, you can redirect stdout to a file.'''

import sys

# Redirect stdout to a file
sys.stdout = open("output.txt", "w")

# All print statements will now go to the file
print("This will be written to output.txt")

'''8. Saving Output to a Database (SQLite)
You can save data to an SQLite database using the sqlite3 module.'''

import sqlite3

# Connect to (or create) an SQLite database
conn = sqlite3.connect('output.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)''')

# Insert data
cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', ("Alice", 30))

# Commit and close
conn.commit()
conn.close()
