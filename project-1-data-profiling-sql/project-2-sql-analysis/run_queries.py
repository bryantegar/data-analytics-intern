import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")

print("\nTOTAL REVENUE")
q1 = "SELECT SUM(price*quantity) AS total_revenue FROM sales"
print(pd.read_sql(q1, conn))

print("\nTOP PRODUCT")
q2 = """
SELECT product, SUM(quantity) as total_sold
FROM sales
GROUP BY product
ORDER BY total_sold DESC
"""
print(pd.read_sql(q2, conn))

print("\nREVENUE PER CATEGORY")
q3 = """
SELECT category, SUM(price*quantity) as revenue
FROM sales
GROUP BY category
"""
print(pd.read_sql(q3, conn))

conn.close()
