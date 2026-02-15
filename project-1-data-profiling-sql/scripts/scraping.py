import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://example.com/harga-pangan"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

data = []
items = soup.find_all("tr")

for item in items:
    cols = item.find_all("td")
    if len(cols) > 0:
        nama = cols[0].text.strip()
        harga = cols[1].text.strip()
        data.append([nama, harga])

df = pd.DataFrame(data, columns=["Komoditas","Harga"])
df.to_csv("data_raw/harga_pangan.csv", index=False)

print("Scraping selesai!")
