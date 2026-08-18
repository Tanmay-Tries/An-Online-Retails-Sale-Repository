import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Display all columns.
pd.set_option("display.max_columns", None)

# Read dataset
df = pd.read_csv("online_retail_clean.csv")

# Convert InvoiceDate into datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Feature Engineering
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month_name()
df["Day"] = df["InvoiceDate"].dt.day
df["Weekday"] = df["InvoiceDate"].dt.day_name()
df["Hour"] = df["InvoiceDate"].dt.hour

top_products = (
    df.groupby("Description")["Quantity"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))
sns.barplot(
    x=top_products.values,
    y=top_products.index
)

plt.title("Top 10 Selling Products")
plt.xlabel("Quantity Sold")
plt.ylabel("Product")
plt.show()

#Top 10 sales of countries by Revenue
plt.figure(figsize=(10,6))
sns.barplot(
    x=country_sales.values,
    y=country_sales.index
)

plt.title("Top Countries by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Country")
plt.show()

#orders by Country
plt.figure(figsize=(12,6))

sns.countplot(
    y="Country",
    data=df,
    order=df["Country"].value_counts().index
)

plt.title("Orders by Country")
plt.show()

#monthly revenue trend
monthly_sales = (
    df.groupby("Month")["Revenue"]
      .sum()
      .reindex([
          "January","February","March","April","May","June",
          "July","August","September","October","November","December"
      ])
)
plt.figure(figsize=(12,5))
plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)
plt.xticks(rotation=45)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()

#Orders by Hour
hourly = df.groupby("Hour").size()
plt.figure(figsize=(10,5))
plt.plot(
    hourly.index,
    hourly.values,
    marker="o"
)
plt.title("Orders by Hour")
plt.xlabel("Hour")
plt.ylabel("Orders")
plt.grid(True)
plt.show()

#Quantity Distribution
plt.figure(figsize=(8,5))
plt.hist(
    df["Quantity"],
    bins=30
)
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()

#Unit Price Distribution
plt.figure(figsize=(8,5))
plt.hist(
    df["UnitPrice"],
    bins=30
)
plt.title("Unit Price Distribution")
plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.show()
