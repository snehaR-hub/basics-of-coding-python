Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''In Python, comments are used to add explanatory notes within the code. These comments help you or others understand the code more easily and don't affect the program's execution.'''
... 
... #There are two main types of comments in Python:
... 
... '''1. Single-line comments
... Single-line comments start with the hash symbol (#). Everything following the # on that line is treated as a comment and ignored by the Python interpreter.
... 
... Example:
... python'''
... 
... # This is a single-line comment
... x = 10  # This is also a comment, placed at the end of a line of code
... '''2. Multi-line comments (Block comments)
... Python doesn't have a specific syntax for multi-line comments, but you can achieve multi-line comments in two main ways:
... 
... a. Consecutive single-line comments:
... '''
... # This is a multi-line comment
... # that spans multiple lines.
... # Each line starts with a '#'.
... '''b. Using triple quotes (''' or """):
... While triple quotes are usually used for docstrings (used to document functions, classes, and modules), they can also be used to create multi-line comments. However, this is not the recommended practice for comments, as it's primarily intended for documentation.'''
... 
... '''
... This is a multi-line comment
... that spans several lines.
... Python ignores it during execution.
