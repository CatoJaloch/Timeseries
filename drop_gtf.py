import pandas as pd
import os

folder = "weekly_outputs"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        file_path = os.path.join(folder, file)

        df = pd.read_csv(file_path)

        # Drop rows where farm_name is gtf_variety
        df = df[df["farm_name"] != "gtf_variety"]

        # Save back
        df.to_csv(file_path, index=False)

print("Done removing gtf_variety rows.")