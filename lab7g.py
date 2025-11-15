# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: syed mujeeb
# Date:
# Purpose: Create data frame from CSV file.
# Usage: ./lab10g.py


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("=== lab7g.py ===\n")

# 1) Load data from GitHub raw CSV (IMDB Top 250 dataset link given in lab)
csv_url = "https://raw.githubusercontent.com/itiievskyi/IMDB-Top-250/master/imdb_top_250.csv"
try:
    df = pd.read_csv(csv_url)
    print("CSV loaded successfully from GitHub raw URL.")
except Exception as e:
    print("Error loading CSV from URL:", e)
    raise

# Show basic info
print("\nDataFrame info:")
print(df.info())

# Print summary of the data contained in data frame
print("\nSummary statistics (describe):\n", df.describe(include='all'))

# Print first 10 and last 10 rows
print("\nFirst 10 rows:\n", df.head(10))
print("\nLast 10 rows:\n", df.tail(10))

# Prepare/clean Year column: try to extract a 4-digit year and convert to int
if "Year" in df.columns:
    df["Year_clean"] = df["Year"].astype(str).str.extract(r'(\d{4})')
    df["Year_clean"] = pd.to_numeric(df["Year_clean"], errors='coerce').astype('Int64')
else:
    # Try to find a column name containing 'year'
    year_cols = [c for c in df.columns if 'year' in c.lower()]
    if year_cols:
        col = year_cols[0]
        df["Year_clean"] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
    else:
        df["Year_clean"] = pd.NA

print("\nEarliest movie year (min) and latest movie year (max):")
try:
    earliest = int(df["Year_clean"].min())
    latest = int(df["Year_clean"].max())
    print("Earliest:", earliest, " Latest:", latest)
except Exception as e:
    print("Could not compute earliest/latest year:", e)

# Print unique values in the "Genre" column (if present)
genre_cols = [c for c in df.columns if 'genre' in c.lower()]
if genre_cols:
    gcol = genre_cols[0]
    unique_genres = df[gcol].dropna().unique()
    print(f"\nUnique values in '{gcol}' column (sample):", unique_genres[:20])
else:
    print("\nNo 'Genre' column found in dataset.")

# Count how many movies are not made in USA
# Find a country-like column
country_cols = [c for c in df.columns if 'country' in c.lower()]
if country_cols:
    ccol = country_cols[0]
    # Count rows where country does not contain 'USA' (case-insensitive)
    not_usa_mask = ~df[ccol].astype(str).str.contains('USA', case=False, na=False)
    count_not_usa = int(not_usa_mask.sum())
    print(f"\nNumber of movies not made in USA (based on column '{ccol}'): {count_not_usa}")
else:
    print("\nNo 'Country' column found; cannot count movies not made in USA from this dataset.")

# Find top 10 Highest-Rated Movies
# Try to detect rating column name
rating_cols = [c for c in df.columns if 'rating' in c.lower() or 'imdb' in c.lower()]
if rating_cols:
    rcol = rating_cols[0]
    top10 = df.sort_values(by=rcol, ascending=False).head(10)
    print(f"\nTop 10 movies by '{rcol}':\n", top10[[c for c in df.columns if c in [rcol, 'Title', 'Title\n', 'name', 'Name'] or True]].head(10))
else:
    # Try numeric columns for rating-like values
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if numeric_cols:
        rcol = numeric_cols[0]
        top10 = df.sort_values(by=rcol, ascending=False).head(10)
        print(f"\nTop 10 movies by numeric column '{rcol}':\n", top10.head(10))
    else:
        print("\nCould not detect a rating column to find top 10 highest-rated movies.")

# Best decade of movies (by mean rating) and scatter plot
# We need a numeric year and numeric rating column for this
# For rating, try rcol assigned above; for year use Year_clean
if "Year_clean" in df.columns and (rcol is not None):
    # Ensure rating is numeric
    df['rating_numeric'] = pd.to_numeric(df[rcol], errors='coerce')
    # Drop rows where either value missing
    tmp = df.dropna(subset=['Year_clean', 'rating_numeric'])
    if not tmp.empty:
        def get_decade(y):
            return int((y // 10) * 10)
        tmp['Decade'] = tmp['Year_clean'].apply(get_decade)
        decade_group = tmp.groupby('Decade')['rating_numeric'].mean().reset_index()
        decade_group_sorted = decade_group.sort_values('Decade')
        print("\nMean rating by decade:\n", decade_group_sorted)
        # Best decade
        best_row = decade_group_sorted.loc[decade_group_sorted['rating_numeric'].idxmax()]
        print("\nBest decade (highest mean rating):", int(best_row['Decade']), "with mean rating", float(best_row['rating_numeric']))

        # Scatter plot: Decade vs mean rating
        plt.figure(figsize=(8,5))
        plt.scatter(decade_group_sorted['Decade'], decade_group_sorted['rating_numeric'])
        plt.xlabel('Decade')
        plt.ylabel('Mean Rating')
        plt.title('Mean Movie Rating by Decade (IMDB Top 250 data)')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("decade_scatter.png")
        print("\nSaved scatter plot to 'decade_scatter.png'.")
        plt.show()
    else:
        print("\nNot enough data to compute decade statistics.")
else:
    print("\nCould not compute decade stats (missing Year_clean or rating column).")
