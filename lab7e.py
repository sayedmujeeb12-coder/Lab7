# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: syed mujeeb
# Date:
# Purpose: Create Series.
# Usage: ./lab10e.py

import pandas as pd

print("=== lab7e.py ===\n")

values = ["<50", "50-59", "60-69", "70-79", "80-89", "90-100"]
indices = ["F", "D", "C", "B", "A", "A+"]

grade_series = pd.Series(values, index=indices)
print("Grade series:\n", grade_series)

# Print the values of indices "C" and "A+"
print("\nValue at index 'C':", grade_series["C"])
print("Value at index 'A+':", grade_series["A+"])

# Print value "60-69" directly without printing its index name
# We can get it by position (index 2) or by label "C"
value_60_69 = grade_series.iloc[2]   # or grade_series['C']
print("\nValue (60-69) accessed directly (no index label shown):", value_60_69)

# Show the '*' operation on this list/series.
# For strings, Series * 2 repeats each string twice (element-wise)
print("\nDemonstrating the '*' operation (series * 2):\n", grade_series * 2)
