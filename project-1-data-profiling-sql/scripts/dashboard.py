import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data_clean", "kurs_usd_idr_clean.csv")

df = pd.read_csv(file_path)

df["Tanggal"] = pd.to_datetime(df["Tanggal"])

plt.figure()
plt.plot(df["Tanggal"], df["Kurs"])
plt.title("Trend Kurs USD ke IDR")
plt.xlabel("Tanggal")
plt.ylabel("Kurs")
plt.xticks(rotation=45)

output_path = os.path.join(BASE_DIR, "kurs_chart.png")
plt.savefig(output_path, bbox_inches="tight")

print("Grafik berhasil dibuat!")
