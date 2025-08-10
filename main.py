import pandas as pd

# read excel, then convert to csv file
df= pd.read_excel("sample.xlsx")
df.to_csv("sample.csv")

# no.1 find all rows with country paramether == united kingdom
print(df.where(df["Country"]=="United Kingdom").dropna())
# no.2 find all rows with country == UK and price of over 8
mask = (df["Country"] == "United Kingdom") & (df["UnitPrice"] > 8)
print(df.where(mask).dropna())
# no.3 find all rows to show products with price < 1
print(df.where(df["UnitPrice"]<1).dropna())
# no.4 find all rows with negative quanitity
print(df.where(df["Quantity"]<0).dropna())
# no.5 products with StockCode starting with "85"
print(df.where(df["StockCode"].astype(str).str.startswith("85")).dropna())
# no.6 products with quantity between 5 and 5
mask2= ((df["Quantity"]<15) & (df["Quantity"]>5))
print(df.where(mask2).dropna())
# no.7 products with description ending with "HOLDER"
print(df.where(df["Description"].astype(str).str.endswith("HOLDER")).dropna())
# no.8 Show invoices where UnitPrice is greater than the average UnitPrice of all products
print(df["InvoiceNo"].where(df["UnitPrice"]>df["UnitPrice"].mean()).dropna())
# no.9 From customers in France, find the top product by quantity sold
mask3= (df["Country"]=="France") & (df["Quantity"]==df["Quantity"].max())
print(df.where(mask3).dropna())
# no. 10 invoices where the total price (Quantity × UnitPrice) is greater than 50
print(df["InvoiceNo"].where((df["Quantity"]*df["UnitPrice"])>50).dropna())

