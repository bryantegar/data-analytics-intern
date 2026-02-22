import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/customer.csv")

# convert kategori → numerik
df["gender"] = df["gender"].map({"Male":1,"Female":0})
df["city"] = df["city"].astype("category").cat.codes

X = df[["age","gender","city"]]
y = df["purchase"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

score = model.score(X_test,y_test)

print("Model Accuracy:", score)

# contoh prediksi
sample = [[30,1,1]]
pred = model.predict(sample)
print("Predicted purchase:", pred[0])
