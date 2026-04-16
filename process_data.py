import pandas as pd

df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([df1, df2, df3], ignore_index=True)

df = df[df["product"] == "pink morsel"].copy()
df["price"] = df["price"].replace("[$,]", "", regex=True).astype(float)
df["quantity"] = pd.to_numeric(df["quantity"])
df["sales"] = df["quantity"] * df["price"]

df = df[["sales", "date", "region"]]

df.to_csv("cleaned_data.csv", index=False)

print("done - cleaned_data.csv created")