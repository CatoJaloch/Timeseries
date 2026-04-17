import pandas as pd
import os

folder = "gtf_weekly_outputs"

# --- Compute error metrics and unpredictability ranking per week ---

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)

        df = pd.read_csv(path)
        df.columns = df.columns.str.strip().str.lower()

        # Step 1: Signed accuracy
        # Positive = forecast exceeded harvest (overforecast)
        # Negative = forecast fell short of harvest (underforecast)
        df["perc_accuracy"] = (
            (df["field_forecasts"] - df["field_harvests"])
            / df["field_harvests"]
        )

        df["perc_accuracy"] = df["perc_accuracy"].replace(
            [float("inf"), -float("inf")], None
        )

        # Step 2: Absolute percentage error — magnitude of miss, direction removed
        df["abs_perc_error"] = df["perc_accuracy"].abs()

        # Step 3: Weighted absolute error — scales each row's error by actual
        # stems harvested so low-volume fields don't distort the ranking.
        # A 50% error on 50 stems scores 25; the same error on 5,000 stems scores 2,500.
        df["weighted_abs_perc_error"] = df["abs_perc_error"] * df["field_harvests"]

        # Rank driven by weighted error — field size is factored in
        df = df.sort_values(by="weighted_abs_perc_error", ascending=False)
        df["unpredictability_rank"] = range(1, len(df) + 1)

        # Keep only the columns relevant to the weekly output
        df = df[[
            "week_number", "variety_id", "variety_name", "field",
            "field_forecasts", "field_harvests", "forecast_type",
            "abs_perc_error", "weighted_abs_perc_error", "unpredictability_rank"
        ]]

        df.to_csv(path, index=False)
        print(f"Processed: {file}")

print("All gtf weekly files processed successfully.")
