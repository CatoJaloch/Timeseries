import pandas as pd
import os

# Load lookup tables
sian_variety = pd.read_csv("sian_variety.csv")
sian_field = pd.read_csv("sian_field.csv")

# Clean column names
sian_variety.columns = sian_variety.columns.str.strip().str.lower()
sian_field.columns = sian_field.columns.str.strip().str.lower()

# Only what we need
sian_variety_lookup = sian_variety[[
    "week_number", "variety_name", "field"
]]

sian_field_lookup = sian_field[[
    "variety_name", "field", "variety_id", "area_msqr", "type"
]]
#clean names
for df_ in [sian_variety_lookup, sian_field_lookup]:
    df_["variety_name"] = df_["variety_name"].str.strip()
    df_["field"] = df_["field"].str.strip()

folder = "weekly_outputs"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        # Clean
        df.columns = df.columns.str.strip().str.lower()
        df["variety_name"] = df["variety_name"].str.strip()

        # ---------------------------------------------------
        # STEP A: Add FIELD (from sian_variety)
        # ---------------------------------------------------
        df = df.merge(
            sian_variety_lookup,
            on=["week_number", "variety_name"],
            how="left"
        )

        # ---------------------------------------------------
        # STEP B: Add variety_id, area, type (from sian_field)
        # ---------------------------------------------------
        df = df.merge(
            sian_field_lookup,
            on=["variety_name", "field"],
            how="left"
        )

        # Save back
        df.to_csv(path, index=False)

print("All weekly files updated successfully.")    