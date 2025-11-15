# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: syed mujeeb
# Date:
# Purpose: Slice NumPy Arrays.
# Usage: ./lab10c.py
import numpy as np

print("=== lab7c.py ===\n")

# Create a 1D array numArray initialized with 100 random numbers
# (use uniform on [0,1) for demonstration)
np.random.seed(1)
numArray = np.random.rand(100)

print("numArray length:", numArray.size)

# Slice and print first 10 values
first_10 = numArray[:10]
print("\nFirst 10 values:\n", first_10)

# Slice and print last 10 values
last_10 = numArray[-10:]
print("\nLast 10 values:\n", last_10)

# Slice and print 30 values starting from index 21 (i.e., indices 21..50 exclusive -> 21..50 = 30 values)
slice_21_30 = numArray[21:21+30]
print("\n30 values starting from index 21 (indices 21..50):\n", slice_21_30)

# With one statement, change all values to 101 from index 50 to 65 (inclusive)
# Python slice end is exclusive, so we assign to [50:66]
numArray[50:66] = 101
print("\nAfter setting indices 50..65 to 101, slice 48..68:\n", numArray[48:69])
