import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Rutas a los CSV
csv_a = "Eval-DRL-Baseline-2026-case-2_2025-12-17_10:31-res1/progress.csv"
csv_b = "degradations/Eval-DRL-Baseline-2026-case-2-all_2_2025-12-17_13:10-res1/progress.csv"

# Cargar datos
df_a = pd.read_csv(csv_a)
df_b = pd.read_csv(csv_b)

# Métricas a comparar: (label, column_name, output_file)
metrics = [
    (
        "Mean temperature violation (ºC)",
        "mean_temperature_violation",
        "mean_temperature_violation.png",
    ),
    ("Mean power demand (kW)", "mean_power_demand", "mean_power_demand.png"),
    (
        "Mean daily compressor starts",
        "mean_compressor_starts_per_day",
        "mean_compressor_starts.png",
    ),
]

labels = ["Default", "Degraded"]
x = np.arange(len(labels))
width = 0.6

for title, column, output_path in metrics:
    values = [df_a[column].mean(), df_b[column].mean()]

    plt.figure(figsize=(5, 4))
    plt.bar(x, values, width)

    plt.xticks(x, labels)
    plt.ylabel(title)
    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()
