import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
input_path = os.path.join(BASE_DIR, "data_raw", "kurs_usd_idr.csv")

df = pd.read_csv(input_path)

df["Kurs"] = df["Kurs"].astype(float)
df = df.sort_values("Tanggal")

output_path = os.path.join(BASE_DIR, "data_clean", "kurs_usd_idr_clean.csv")
df.to_csv(output_path, index=False)

print("Cleaning selesai!")
