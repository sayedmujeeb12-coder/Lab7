# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: syed mujeeb
# Date:
# Purpose: Create Data Frames.
# Usage: ./lab10f.py
import pandas as pd

print("=== lab7f.py ===\n")

# Given dictionaries (first three)
d1 = {"Apple": "Green", "Carrot": "Red", "Radish": "Purple"}
d2 = {"Okra": "Thin", "Potato": "blob", "Radish": "Round"}
d3 = {"Apple": 2.1, "Okra": 3.5, "Carrot": 1.3, "Potato": 2.0, "Radish": 3.0}

# Create DataFrames from each dictionary and print
df_colors = pd.DataFrame(list(d1.items()), columns=["Item", "Color"])
df_shape = pd.DataFrame(list(d2.items()), columns=["Item", "Shape"])
df_price = pd.DataFrame(list(d3.items()), columns=["Item", "Price"])

print("DataFrame from d1 (colors):\n", df_colors)
print("\nDataFrame from d2 (shapes):\n", df_shape)
print("\nDataFrame from d3 (prices):\n", df_price)

# Combine into a single DataFrame (index by Item)
combined = pd.DataFrame.from_dict(d1, orient='index', columns=["Color"])
combined["Shape"] = pd.Series(d2)
combined["Price"] = pd.Series(d3)
combined = combined.reset_index().rename(columns={"index": "Item"})
print("\nCombined DataFrame (Item / Color / Shape / Price):\n", combined)

# Create a DataFrame that resembles a simple tabular layout (placeholder for dataframe.jpg)
# Since we can't see the image here, create a small example dataframe with clear columns:
example_df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 27, 22],
    "City": ["New York", "Los Angeles", "Chicago"]
})
print("\nExample DataFrame (placeholder for dataframe.jpg):\n", example_df)


