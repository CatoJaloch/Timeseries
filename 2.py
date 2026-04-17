import pandas as pd
import os

# --- Clean source data: remove zero-harvest and zero-forecast rows ---

df = pd.read_csv('gtf_variety.csv')
df.drop(df[df["field_harvests"] == 0].index, inplace=True)
df.drop(df[df["field_forecasts"] == 0].index, inplace=True)
df.to_csv('gtf_variety.csv', index=False)

week_numbers = df['week_number'].unique()
print("Available week numbers GTF:", week_numbers)


# --- Load and prepare GTF data ---
# Only the columns needed for weighted error calculations are carried
# into the weekly outputs — the full source file remains untouched.

def process_file(file_name, farm_name):
    df = pd.read_csv(file_name)
    df.columns = df.columns.str.strip().str.lower()

    df = df[[
        "week_number", "variety_id", "variety_name", "field",
        "field_forecasts", "field_harvests", "forecast_type"
    ]]

    df["farm_name"] = farm_name
    df["week_number"] = pd.to_numeric(df["week_number"], errors="coerce")

    return df


df_gtf = process_file("gtf_variety.csv", "gtf_variety")

# Season spans two calendar years — ordering must follow harvest cycle,
# not ascending calendar order
week_order = [45, 46, 47, 48, 49, 50, 51, 52,
              1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]

df_gtf["week_number"] = pd.Categorical(
    df_gtf["week_number"], categories=week_order, ordered=True
)
df_gtf = df_gtf.sort_values("week_number")

os.makedirs("gtf_weekly_outputs", exist_ok=True)

for week in week_order:
    week_df = df_gtf[df_gtf["week_number"] == week]
    if not week_df.empty:
        week_df.to_csv(f"gtf_weekly_outputs/week_{week}.csv", index=False)

print("GTF weekly output files created.")
