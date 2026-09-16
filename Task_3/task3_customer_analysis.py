import pandas as pd

# Load the dataset
df = pd.read_csv("customer_data.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# Purchasing Behavior Analysis

print("\n========== PURCHASING BEHAVIOR ANALYSIS ==========")

# Total customers
print("\nTotal Customers:")
print(df["Customer_ID"].nunique())

# Total orders
print("\nTotal Orders:")
print(df["Total_Orders"].sum())

# Total customer spending
print("\nTotal Customer Spending:")
print(round(df["Total_Spend"].sum(), 2))

# Average order value
print("\nAverage Order Value:")
print(round(df["Avg_Order_Value"].mean(), 2))

# Orders by product category
print("\nOrders by Product Category:")
print(df["Product_Category"].value_counts())

# Customers by customer type
print("\nCustomers by Customer Type:")
print(df["Customer_Type"].value_counts())

# Customers by purchase frequency
print("\nCustomers by Purchase Frequency:")
print(df["Purchase_Frequency"].value_counts())

#  Age Segmentation

print("\n========== AGE SEGMENTATION ==========")

# Number of customers in each age group
print("\nCustomers by Age Group:")
print(df["Age_Group"].value_counts().sort_index())

# Total spending by age group
print("\nTotal Spending by Age Group:")
print(df.groupby("Age_Group", observed=True)["Total_Spend"].sum().round(2))

# Average spending by age group
print("\nAverage Spending by Age Group:")
print(df.groupby("Age_Group", observed=True)["Total_Spend"].mean().round(2))

#  Location Segmentation

print("\n========== LOCATION SEGMENTATION ==========")

# Number of customers by location
print("\nCustomers by Location:")
print(df["Location"].value_counts())

# Total spending by location
print("\nTotal Spending by Location:")
print(df.groupby("Location")["Total_Spend"].sum().sort_values(ascending=False).round(2))

# Average spending by location
print("\nAverage Spending by Location:")
print(df.groupby("Location")["Total_Spend"].mean().sort_values(ascending=False).round(2))

# Buying Pattern Segmentation

print("\n========== BUYING PATTERN SEGMENTATION ==========")

# Number of customers by purchase frequency
print("\nCustomers by Purchase Frequency:")
print(df["Purchase_Frequency"].value_counts())

# Total spending by purchase frequency
print("\nTotal Spending by Purchase Frequency:")
print(
    df.groupby("Purchase_Frequency", observed=True)["Total_Spend"]
      .sum()
      .sort_values(ascending=False)
      .round(2)
)

# Average spending by purchase frequency
print("\nAverage Spending by Purchase Frequency:")
print(
    df.groupby("Purchase_Frequency", observed=True)["Total_Spend"]
      .mean()
      .sort_values(ascending=False)
      .round(2)
)

# Total spending by customer type
print("\nTotal Spending by Customer Type:")
print(
    df.groupby("Customer_Type")["Total_Spend"]
      .sum()
      .sort_values(ascending=False)
      .round(2)
)

#  Most Valuable Customer Groups

print("\n========== MOST VALUABLE CUSTOMER GROUPS ==========")

# Top 10 individual customers by total spending
print("\nTop 10 Customers by Total Spend:")
print(
    df[["Customer_ID", "Age", "Location", "Customer_Type",
        "Total_Orders", "Total_Spend", "Product_Category"]]
    .sort_values("Total_Spend", ascending=False)
    .head(10)
)

# Total spending by product category
print("\nTotal Spending by Product Category:")
print(
    df.groupby("Product_Category")["Total_Spend"]
      .sum()
      .sort_values(ascending=False)
      .round(2)
)

# Total spending by customer type
print("\nTotal Spending by Customer Type:")
print(
    df.groupby("Customer_Type")["Total_Spend"]
      .sum()
      .sort_values(ascending=False)
      .round(2)
)

# Total spending by age group
print("\nTotal Spending by Age Group:")
print(
    df.groupby("Age_Group", observed=True)["Total_Spend"]
      .sum()
      .sort_values(ascending=False)
      .round(2)
)

# Total spending by purchase frequency
print("\nTotal Spending by Purchase Frequency:")
print(
    df.groupby("Purchase_Frequency", observed=True)["Total_Spend"]
      .sum()
      .sort_values(ascending=False)
      .round(2)
)

import matplotlib.pyplot as plt


# Customer Visualizations

# 1. Customers by Age Group
age_counts = df["Age_Group"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
age_counts.plot(kind="bar")
plt.title("Customers by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 2. Total Spending by Location
location_spend = df.groupby("Location")["Total_Spend"].sum().sort_values(ascending=False)

plt.figure(figsize=(9, 5))
location_spend.plot(kind="bar")
plt.title("Total Spending by Location")
plt.xlabel("Location")
plt.ylabel("Total Spend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 3. Total Spending by Product Category
category_spend = df.groupby("Product_Category")["Total_Spend"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
category_spend.plot(kind="bar")
plt.title("Total Spending by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Spend")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()


# 4. Customers by Purchase Frequency
frequency_counts = df["Purchase_Frequency"].value_counts()

plt.figure(figsize=(8, 5))
frequency_counts.plot(kind="bar")
plt.title("Customers by Purchase Frequency")
plt.xlabel("Purchase Frequency")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 5. Total Spending by Customer Type
type_spend = df.groupby("Customer_Type")["Total_Spend"].sum()

plt.figure(figsize=(7, 5))
type_spend.plot(kind="bar")
plt.title("Total Spending by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Total Spend")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Customer Insights and Marketing Strategies

print("\n========== CUSTOMER INSIGHTS ==========")

# Highest spending location
top_location = df.groupby("Location")["Total_Spend"].sum().idxmax()
print("\nHighest Spending Location:", top_location)

# Highest spending product category
top_category = df.groupby("Product_Category")["Total_Spend"].sum().idxmax()
print("Highest Spending Product Category:", top_category)

# Highest spending age group
top_age_group = df.groupby("Age_Group", observed=True)["Total_Spend"].sum().idxmax()
print("Highest Spending Age Group:", top_age_group)

# Highest spending customer type
top_customer_type = df.groupby("Customer_Type")["Total_Spend"].sum().idxmax()
print("Highest Spending Customer Type:", top_customer_type)

# Highest spending purchase frequency
top_frequency = df.groupby("Purchase_Frequency", observed=True)["Total_Spend"].sum().idxmax()
print("Highest Spending Purchase Frequency:", top_frequency)

# Most common product category
popular_category = df["Product_Category"].value_counts().idxmax()
print("Most Popular Product Category:", popular_category)


print("\n========== MARKETING STRATEGIES ==========")

print("""
1. High-Value Customers:
   Offer loyalty rewards, exclusive deals, and early access to new products.

2. Returning Customers:
   Use personalized recommendations and loyalty programs to encourage repeat purchases.

3. Low-Frequency Customers:
   Use targeted discounts, reminder campaigns, and personalized offers to increase purchase frequency.

4. High-Spending Locations:
   Focus regional promotions and advertising campaigns in high-revenue locations.

5. Popular Product Categories:
   Promote best-selling categories through bundles, cross-selling, and personalized recommendations.

6. Younger Customers:
   Use social media campaigns, limited-time offers, and mobile-friendly promotions.

7. Older Customer Groups:
   Focus on loyalty benefits, product quality, and personalized communication.
""")