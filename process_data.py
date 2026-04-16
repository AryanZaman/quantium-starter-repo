import pandas as pd

# load all files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# combine them
df = pd.concat([df1, df2, df3])

# filter only Pink Morsels
df = df[df["product"] == "pink morsel"]

# create sales column
df["sales"] = df["quantity"] * df["price"]

# keep only required columns
df = df[["sales", "date", "region"]]

# save output
df.to_csv("cleaned_data.csv", index=False)

print("done - cleaned_data.csv created")