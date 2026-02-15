import pandas as pd

df = pd.read_csv("data_raw/harga_pangan.csv")

df["Harga"] = df["Harga"].str.replace("Rp","").str.replace(".","").astype(int)

df = df.drop_duplicates()

df.to_csv("data_clean/harga_pangan_clean.csv", index=False)

print("Cleaning selesai!")
