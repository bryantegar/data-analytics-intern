import pandas as pd

df = pd.read_csv("data/customer_data.csv")

print("DATASET INFO")
print(df.info())

print("\nSTATISTICS")
print(df.describe())

print("\nAVG PURCHASE BY CITY")
print(df.groupby("city")["purchase_amount"].mean())

print("\nAVG PURCHASE BY GENDER")
print(df.groupby("gender")["purchase_amount"].mean())

print("\nTOP 3 SPENDERS")
print(df.sort_values("purchase_amount", ascending=False).head(3))
