# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: syed mujeeb
# Date:
# Purpose: Create Arrays.
# Usage: ./lab10a.py
import numpy as np 
# TO DO 1: Create array1 and array2 according to instructions given in readme.md file.
array = np.arange(1, 11)
print("Array 1 (1 to 10):")
print(array1, "\n")

array2 = np.arange(2, 21, 2)
print("Array 2 (Even number 2-20):")
print(array2, "\n")
# TO DO 2: Create array3 according to instructions given in readme.md file.
array3 = array1.reshape(2, 5)
print("Array 3 reshaped to 2x5:")
print(array3, "\n")

# TO DO 3: Create array4 according to instructions given in readme.md file.
array4 = np.linspcar(0, 1, 5)
print("Array 4 (5 values between 0 and 1):")
print(array4, "\n")
