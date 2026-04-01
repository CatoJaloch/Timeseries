import pandas as pd
#read csv
df = pd.read_csv('sian_variety.csv')
df.drop(df[df["field_harvests"] == 0].index, inplace=True)
df.drop(df[df["field_forecasts"] == 0].index, inplace=True)
df.to_csv('sian_variety.csv', index=False)
# listing the  week numbers available for use
week_numbers = df['week_number'].unique()
print("Available week numbers Sian:", week_numbers)
#Available week numbers: [45 46 47 48 49 50 51 52  1  2  3  4  5  6  7  8  9 10 11]

#read csv
df = pd.read_csv('gtf_variety.csv')
df.drop(df[df["field_harvests"] == 0].index, inplace=True)
df.drop(df[df["field_forecasts"] == 0].index, inplace=True)
df.to_csv('gtf_variety.csv', index=False)
# listing the  week numbers available for use
week_numbers = df['week_number'].unique()
print("Available week numbers GTF:", week_numbers)
#Available week numbers GTF: [45 46 47 48 49 50 51 52  1  2  3  4  5  6  7  8  9 10 11]

import pandas as pd
import os

def process_file(file_name, farm_name):
    df = pd.read_csv(file_name)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Rename column
    df = df.rename(columns={"field_forecasts": "field_forecasts"})

    # Keep only needed columns
    df = df[["week_number", "variety_name", "field_forecasts", "field_harvests"]]

    # Add farm name column
    df["farm_name"] = farm_name

    # Ensure week is numeric
    df["week_number"] = pd.to_numeric(df["week_number"], errors="coerce")

    return df


# Process both files
df_sian = process_file("sian_variety.csv", "sian_variety")
df_gtf = process_file("gtf_variety.csv", "gtf_variety")

# Combine both datasets
df = pd.concat([df_sian, df_gtf], ignore_index=True)

# Custom week order
week_order = [45, 46, 47, 48, 49, 50, 51, 52,
              1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Apply ordering
df["week_number"] = pd.Categorical(df["week_number"], categories=week_order, ordered=True)

# Sort
df = df.sort_values("week_number") 

# Output folder
os.makedirs("weekly_outputs", exist_ok=True)

# Create one file per week (with both farms inside)
for week in week_order:
    week_df = df[df["week_number"] == week]

    if not week_df.empty:
        week_df.to_csv(f"weekly_outputs/week_{week}.csv", index=False)