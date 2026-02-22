import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales.csv")

total_revenue = df["revenue"].sum()
top_product = df.groupby("product")["revenue"].sum().idxmax()
top_city = df.groupby("city")["revenue"].sum().idxmax()

print("=== KPI ===")
print("Total Revenue:", total_revenue)
print("Top Product:", top_product)
print("Top City:", top_city)

# chart revenue per category
df.groupby("category")["revenue"].sum().plot(kind="bar")
plt.title("Revenue by Category")
plt.savefig("revenue_category.png")
