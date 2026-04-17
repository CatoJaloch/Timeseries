import pandas as pd
import os

def process_top6(file_path, farm_name, output_name):
    # Load data
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower()

    # --- Frequency: number of distinct weeks in top 6 ---
    freq = (
        df.groupby("variety_name")["week_number"]
        .nunique()
        .reset_index(name="weeks_in_top6")
    )

    # --- Severity: average weighted error ---
    severity = (
        df.groupby("variety_name")["weighted_avg_abs_perc_error"]
        .mean()
        .reset_index(name="avg_weighted_error")
    )

    # --- Merge both ---
    final = pd.merge(freq, severity, on="variety_name")

    # Add farm label
    final["farm_name"] = farm_name

    # --- Sort: frequency first, then severity ---
    final = final.sort_values(
        by=["weeks_in_top6", "avg_weighted_error"],
        ascending=[False, False]
    ).reset_index(drop=True)

    # Rank
    final["rank"] = range(1, len(final) + 1)

    # Save full ranking
    final.to_csv(output_name, index=False)

    # Also print top 6
    print(f"\nTop 6 for {farm_name}:\n")
    print(final.head(6))


# --- Run for both farms ---

process_top6(
    "sian_weekly_plots/sian_top6.csv",
    "sian",
    "sian_repeat_offenders.csv"
)

process_top6(
    "gtf_weekly_plots/gtf_top6.csv",
    "gtf",
    "gtf_repeat_offenders.csv"
)

print("\nDone. Outputs saved:")
print("- sian_repeat_offenders.csv")
print("- gtf_repeat_offenders.csv")