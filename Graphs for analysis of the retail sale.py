import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Display all columns
pd.set_option("display.max_columns", None)

# Read dataset
df = pd.read_csv("online_retail_clean.csv")

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
