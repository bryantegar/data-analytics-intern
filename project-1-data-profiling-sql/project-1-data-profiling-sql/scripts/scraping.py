import requests
import pandas as pd
import os
from datetime import datetime

url = "https://api.frankfurter.app/latest?from=USD&to=IDR"
response = requests.get(url)
data = response.json()

rate = data["rates"]["IDR"]
date = data["date"]

new_data = pd.DataFrame([{
    "Tanggal": date,
    "Base": "USD",
    "Target": "IDR",
    "Kurs": rate,
    "Timestamp": datetime.now()
}])

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data_raw", "kurs_usd_idr.csv")

if os.path.exists(file_path):
    old = pd.read_csv(file_path)
    df = pd.concat([old, new_data])
else:
    df = new_data

df = df.drop_duplicates(subset=["Tanggal"])

df.to_csv(file_path, index=False)

print("Data berhasil diperbarui!")
