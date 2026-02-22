import sqlite3
import pandas as pd

df = pd.read_csv("data/sales.csv")

conn = sqlite3.connect("sales.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

conn.close()

print("Database berhasil dibuat!")
