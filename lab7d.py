# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: syed mujeeb
# Date:
# Purpose: Slice 2D NumPy Arrays.
# Usage: ./lab10d.py

import numpy as np

print("=== lab7d.py ===\n")

# Given 2D array
arr_2d = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]
])

print("Original arr_2d:\n", arr_2d)

# Slice the first two rows and the last three columns -> slice_1
slice_1 = arr_2d[:2, -3:]
print("\n slice_1 (first two rows, last three columns):\n", slice_1)

# Extract the middle 2x2 subarray (70,80,120,130) -> slice_2
# Rows 1:3 (i.e., 1 and 2), columns 1:3 (1 and 2)
slice_2 = arr_2d[1:3, 1:3]
print("\n slice_2 (middle 2x2):\n", slice_2)

# Slice every other row and every other column -> slice_3
slice_3 = arr_2d[::2, ::2]
print("\n slice_3 (every other row & column):\n", slice_3)
