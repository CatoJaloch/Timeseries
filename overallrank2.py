import pandas as pd
import os

folder = "gtf_weekly_outputs"
all_data = []

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)
        df = pd.read_csv(path)
        df.columns = df.columns.str.strip().str.lower()
        df = df[["variety_id", "variety_name", "abs_perc_error", "field_harvests"]]
        all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)


# --- Weighted mean absolute error per variety across all weeks ---
#
# Formula: sum(abs_perc_error * field_harvests) / sum(field_harvests)
#
# Normalising by total stems brings the score back to a percentage scale,
# so varieties with more observations aren't penalised simply for having
# more data points. Low-volume fields contribute proportionally less.

def weighted_mean(group):
    weights      = group["field_harvests"]
    errors       = group["abs_perc_error"]
    total_weight = weights.sum()

    if total_weight == 0:
        return pd.Series({
            "variety_name":               group["variety_name"].iloc[0],
            "weighted_avg_abs_perc_error": None,
            "total_stems_observed":        0,
            "observations":                len(group)
        })

    return pd.Series({
        "variety_name":               group["variety_name"].iloc[0],
        "weighted_avg_abs_perc_error": (errors * weights).sum() / total_weight,
        "total_stems_observed":        total_weight,
        "observations":                len(group)
    })


overall_rank = (
    combined_df
    .groupby("variety_id", as_index=False)
    .apply(weighted_mean)
    .sort_values("weighted_avg_abs_perc_error", ascending=False)
    .reset_index(drop=True)
)

overall_rank["overall_rank"] = range(1, len(overall_rank) + 1)
overall_rank.to_csv("gtf_overall_rank.csv", index=False)
print("Created: gtf_overall_rank.csv")
