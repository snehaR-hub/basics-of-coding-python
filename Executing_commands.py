'''In Python, executing commands typically refers to running Python statements or functions that carry out specific actions in your code. You can execute commands in various ways, depending on the environment you're working in (like an interactive Python shell, script, or notebook). Below, I'll cover the different ways of executing commands in Python.

1. Executing Python Commands in an Interactive Shell (REPL)
The Python shell (also known as the REPL - Read Eval Print Loop) allows you to enter Python commands interactively and see immediate results.'''

#Example:

Copy code
$ python
Python 3.x.x (default, ...) ...
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 5
>>> print(x)


'''2. Running Python Code in a Script (from File)
In Python, you can write commands in a script file (typically with the .py extension) and execute them. To do so:

Write your code in a text file (e.g., script.py).
Run the script from the command line or a terminal.'''
#Example
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

'''3. Running Python Code in Jupyter or Google Colab Notebooks
In environments like Jupyter or Google Colab, you can execute commands in code cells. These notebooks allow you to run Python commands interactively, and they show results right below the cell.'''

# In a code cell
x = 10
y = 20
sum_result = x + y
sum_result

'''4. Executing Shell Commands from Python
Python allows you to run system shell commands using the os module or subprocess module. This can be useful when you need to run external commands (like shell commands or scripts) from within your Python code.'''

import os
# Execute a shell command
os.system('echo Hello from the shell!')

'''5. Executing Python Code Dynamically (Using exec() and eval())
Python provides two functions for dynamic execution of Python code:

exec() – Executes Python code dynamically
You can execute a string containing Python code using exec(). This is typically used when you want to evaluate a block of code or a set of commands.'''

code = """
x = 10
y = 20
print(x + y)
"""
exec(code)  # This will print 30

'''6. Running Python Code from an External File (Using runpy)
If you want to execute an entire Python script from within your code, you can use the runpy module.'''

import runpy

# Run a Python script file
runpy.run_path("example.py")

'''7. Executing Python Code Using an IDE or Text Editor
If you're using an Integrated Development Environment (IDE) like PyCharm, VS Code, or Spyder, you can execute Python commands directly from the editor:

Write your code in the editor.
Press a button like Run or use a shortcut (e.g., Shift + F10 in PyCharm) to run the entire script.
The output will be displayed in the terminal or output pane of the IDE.'''

'''8. Executing Asynchronous Code (Using asyncio)
If you have asynchronous code (e.g., using async/await syntax), you can run it using Python's asyncio module.

Example of running an asynchronous function:'''
import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)
    print("World!")

# To run the async function
asyncio.run(say_hello())
