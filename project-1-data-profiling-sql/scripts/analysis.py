import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data_clean", "harga_pangan_clean.csv")

df = pd.read_csv(file_path)

print("Statistik Data:")
print(df.describe())

print("\nKomoditas Termahal:")
print(df.sort_values("Harga", ascending=False).head(3))

print("\nKomoditas Termurah:")
print(df.sort_values("Harga").head(3))
