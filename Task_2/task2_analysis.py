import pandas as pd

df = pd.read_csv("dataset.csv")

print(df)

# Examine the dataset features
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Find Trends & Distributions

print("\nSales by Category:")
print(df["Category"].value_counts())

# Check Sales by Region
print("\nSales by Region:")
print(df["Region"].value_counts())

# Check Sales by Customer Type
print("\nSales by Customer Type:")
print(df["Customer_Type"].value_counts())

# Find the Most Popular Products
print("\nTop 10 Products by Number of Orders:")
print(df["Product"].value_counts().head(10))

# Find Total Revenue by Category
print("\nRevenue by Category:")
print(df.groupby("Category")["Revenue"].sum().sort_values(ascending=False))

# Check Average Revenue by Category
print("\nAverage Revenue by Category:")
print(df.groupby("Category")["Revenue"].mean().sort_values(ascending=False))

# Detect Outliers in Quantity
print("\nQuantity Statistics:")
print(df["Quantity"].describe())

# Detect Revenue Outliers
print("\nRevenue Statistics:")
print(df["Revenue"].describe())

# Check Payment Methods
print("\nOrders by Payment Method:")
print(df["Payment_Method"].value_counts())

# Check Customer Ratings
print("\nCustomer Rating Distribution:")
print(df["Customer_Rating"].value_counts().sort_index())

# Check the Relationship Between Quantity and Revenue
print("\nCorrelation between Quantity and Revenue:")
print(df["Quantity"].corr(df["Revenue"]))

# Check Discount vs Revenue
print("\nCorrelation between Discount and Revenue:")
print(df["Discount_Percent"].corr(df["Revenue"]))

# Find the Best-Selling Category by Quantity
print("\nTotal Quantity Sold by Category:")
print(df.groupby("Category")["Quantity"].sum().sort_values(ascending=False))

# Find the Highest-Revenue Region
print("\nRevenue by Region:")
print(df.groupby("Region")["Revenue"].sum().sort_values(ascending=False))



# BONUS WORK : Create a short report highlighting your findings.

# Create a Findings section
print("\n========== KEY BUSINESS FINDINGS ==========")

print("1. The dataset contains 1000 e-commerce orders.")
print("2. Category, region, customer type, and payment method were analyzed.")
print("3. Revenue and quantity were analyzed to identify sales patterns.")
print("4. Outliers were checked in Quantity and Revenue.")
print("5. Relationships between Quantity, Revenue, and Discount were examined.")