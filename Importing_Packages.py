#1. Importing an Entire Module
import math
print(math.sqrt(16))  # Output: 4.0

#2. Importing Specific Functions/Classes from a Module
from math import sqrt
print(sqrt(16))  # Output: 4.0

#3. Importing with an Alias
import numpy as np
arr = np.array([1, 2, 3])
print(arr)  # Output: [1 2 3]

#4. Importing Multiple Functions
from math import sqrt, pi
print(sqrt(16))  # Output: 4.0
print(pi)        # Output: 3.141592653589793

#5. Importing All Functions/Classes from a Module (Not Recommended)
from math import *
print(sqrt(16))  # Output: 4.0

#6. Importing from a Submodule or Package
#If you have a package with submodules:
import package.submodule

#7. Installing External Packages (Using pip)
#You can install packages that aren't built-in using pip:
#pip install requests
#Then, import and use it in your code:
import requests
response = requests.get('https://www.example.com')
print(response.text)

#8. Checking Installed Packages
pip list  # List installed packages
