# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: syed mujeeb
# Date:
# Purpose: Change Dimensions and create special arrays.
# Usage: ./lab10b.py

import numpy as np

print("=== lab7b.py ===\n")

# Recreate arrays similar to lab7a so we can reshape them here
array1 = np.arange(20, 50)                    # length 30
array2 = np.array(list(range(20, 50)))        # length 30

print("Original array1.shape =", array1.shape)
print("Original array2.shape =", array2.shape)

# Change array1 to 5x6 (5 rows, 6 columns)
array1 = array1.reshape((5, 6))
print("\narray1 reshaped to 5x6:\n", array1)
print("array1.shape =", array1.shape)

# Reshape array2 to 2x3x5 (a 3D matrix)
array2 = array2.reshape((2, 3, 5))
print("\narray2 reshaped to 2x3x5:\n", array2)
print("array2.shape =", array2.shape)

# Create array5: 5x5 diagonal matrix with diagonal (45, 7, 61, 8, 9)
diag_values = (45, 7, 61, 8, 9)
array5 = np.diag(diag_values)
print("\narray5 (5x5 diagonal matrix):\n", array5)

# Create array6: 7x7 matrix sampled from a normal distribution
# (mean 0, std 1) using np.random.randn
np.random.seed(0)  # deterministic for reproducible lab output
array6 = np.random.randn(7, 7)
print("\narray6 (7x7, normal distribution sample):\n", array6)
print("\narray6.shape =", array6.shape)
