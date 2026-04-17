import pandas as pd
import os
import matplotlib.pyplot as plt

folder        = "gtf_weekly_outputs"
output_folder = "gtf_weekly_plots"

os.makedirs(output_folder, exist_ok=True)

all_top6_rows = []   #  collect everything here

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)

        df = pd.read_csv(path)
        df.columns = df.columns.str.strip().str.lower()

        # Extract week number from filename (adjust if your naming differs)
        # Example assumes: week_1.csv, week_2.csv, etc.
        week_number = ''.join([c for c in file if c.isdigit()])
        week_number = int(week_number) if week_number else None

        def weighted_avg(group):
            total_stems = group["field_harvests"].sum()
            if total_stems == 0:
                return pd.Series({
                    "weighted_avg_abs_perc_error": None,
                    "observations": len(group)
                })
            return pd.Series({
                "weighted_avg_abs_perc_error": (
                    group["abs_perc_error"] * group["field_harvests"]
                ).sum() / total_stems,
                "observations": len(group)
            })

        df_avg = (
            df.groupby(["variety_id", "variety_name"])
            .apply(weighted_avg)
            .reset_index()
            .sort_values("weighted_avg_abs_perc_error", ascending=False)
        )

        df_top = df_avg.head(6).copy()
        df_top["week_number"] = week_number   #  add week label

        # keep only needed columns for final CSV
        all_top6_rows.append(
            df_top[["week_number", "variety_name", "weighted_avg_abs_perc_error"]]
        )

        # plotting (unchanged)
        plt.figure()
        plt.barh(df_top["variety_name"], df_top["weighted_avg_abs_perc_error"])

        plt.xlabel("Weighted Average Absolute % Error")
        plt.ylabel("Variety")
        plt.title(f"Top 6 Unpredictable Varieties - {file}")

        plt.gca().invert_yaxis()
        plt.tight_layout()

        save_path = os.path.join(output_folder, file.replace(".csv", ".png"))
        plt.savefig(save_path)
        plt.close()

        print(f"Saved: {save_path}")

#  combine ALL weeks into one CSV
final_df = pd.concat(all_top6_rows, ignore_index=True)
final_df = final_df.sort_values(["week_number", "weighted_avg_abs_perc_error"], ascending=[True, False])

final_csv_path = os.path.join(output_folder, "gtf_top6.csv")
final_df.to_csv(final_csv_path, index=False)

print(f"Saved combined CSV: {final_csv_path}")
print("Done. All gtf weekly plots + gtf_top6.csv created.")