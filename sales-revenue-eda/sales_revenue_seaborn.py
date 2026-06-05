import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("/Users/leelasaigottimukkala/Downloads/SampleSuperstore.csv", encoding='latin1')

# Display first 5 rows
print(df.head())

# Dataset Information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Basic statistics
print(df.describe())

# Total Sales
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# Total Profit
total_profit = df['Profit'].sum()
print("Total Profit:", total_profit)

# Sales by Category
category_sales = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# Top 10 Products
top_products = (
    df.groupby('Product Name')['Sales']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))
top_products.plot(kind='bar')
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Sales Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Sales'], bins=30)
plt.title("Sales Distribution")
plt.show()

# Category Comparison
plt.figure(figsize=(8,5))
sns.boxplot(x='Category', y='Sales', data=df)
plt.title("Category-wise Sales Comparison")
plt.show()

# Correlation Heatmap
numeric_cols = df[['Sales','Profit','Quantity','Discount']]

plt.figure(figsize=(6,4))
sns.heatmap(numeric_cols.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()
