# CODSOFT Task 2 – E-Commerce Sales Analysis

## 📌 Project Overview

This project was completed as part of my **CODSOFT Internship**.

The objective of this task was to analyze an e-commerce sales dataset using **Python and Pandas**, identify important sales trends and distributions, analyze revenue performance, examine potential outliers, and derive practical business insights.

The dataset contains **1,000 e-commerce orders recorded across 2025**.

---

## 🎯 Objectives

* Inspect the structure of the dataset.
* Perform descriptive statistical analysis.
* Analyze sales by product category.
* Analyze revenue by category and region.
* Identify popular products.
* Examine customer types and payment methods.
* Analyze customer rating distribution.
* Check potential outliers in Quantity and Revenue.
* Analyze the relationship between Quantity and Revenue.
* Analyze the relationship between Discount and Revenue.
* Generate business insights and recommendations.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **CSV**
* **Descriptive Statistics**
* **GroupBy Analysis**
* **Correlation Analysis**

---

## 📂 Project Files

| File                | Description                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------- |
| `task2_analysis.py` | Python script containing the complete e-commerce sales analysis                                             |
| `dataset.csv`       | Original e-commerce sales dataset                                                                           |
| `BONUS REPORT.pdf`  | Detailed business-analysis report containing key findings, interpretations, recommendations, and conclusion |
| `README.md`         | Project documentation                                                                                       |

---

## 📊 Dataset Overview

The dataset contains **1,000 e-commerce orders** with information related to transactions, customers, products, pricing, payment methods, and ratings.

### Main Columns

* Order_ID
* Order_Date
* Category
* Product
* Region
* Customer_Type
* Quantity
* Unit_Price
* Discount_Percent
* Revenue
* Payment_Method
* Customer_Rating

---

## 🔍 Analysis Performed

### 1. Dataset Inspection

The dataset was inspected using Pandas to understand its:

* Shape
* Column names
* Data types
* Descriptive statistics

The Python script performs these initial inspection steps before carrying out the analysis.

### 2. Sales by Category

Order counts were analyzed across product categories.

**Key finding:** Fashion recorded the highest number of orders with **223**, followed by Sports with 209, Beauty with 197, Electronics with 192, and Home with 179.

### 3. Revenue by Category

Revenue was grouped by category to identify the strongest revenue-generating product category.

**Key finding:** Electronics generated the highest total revenue at approximately **₹21.82 million**.

| Category    |  Total Revenue |
| ----------- | -------------: |
| Electronics | ₹21,821,749.75 |
| Home        |  ₹5,980,307.15 |
| Sports      |  ₹3,482,830.39 |
| Fashion     |  ₹3,037,052.61 |
| Beauty      |  ₹1,773,920.52 |

### 4. Average Revenue by Category

Average revenue per order was also calculated.

Electronics had the highest average revenue per order at approximately **₹113,655**.

### 5. Revenue by Region

Revenue was analyzed across different regions.

**Key finding:** South generated the highest regional revenue at approximately **₹10.55 million**.

Regional ranking:

1. South – ₹10.55 million
2. West – ₹9.41 million
3. North – ₹8.69 million
4. East – ₹7.45 million

### 6. Popular Products

The analysis identified the **Top 10 products by number of orders** using Pandas value counts.

### 7. Payment Method Analysis

Orders were analyzed according to payment method to understand the distribution of different payment options.

### 8. Customer Rating Analysis

The distribution of customer ratings was analyzed to understand rating patterns within the dataset.

---

## 📈 Outlier Analysis

Quantity and Revenue were examined using descriptive statistics to identify unusually high observations.

The dataset contains intentionally unusual high values, including large order quantities and exceptionally high revenue observations. These were treated as **potential outliers rather than automatically removed**.

In a real-world business scenario, unusual records should be validated against the source system before deciding whether they are errors.

---

## 🔗 Correlation Analysis

### Quantity vs Revenue

The Pearson correlation between Quantity and Revenue was:

**`0.2093`**

This indicates a **weak positive relationship**. Higher quantities tend to be associated with somewhat higher revenue, but quantity alone does not strongly explain revenue.

### Discount vs Revenue

The relationship between Discount Percentage and Revenue was also examined using correlation.

Correlation was used to understand association between the variables; it does not establish causation.

---

## 💡 Key Business Insights

### Electronics is the main revenue driver

Electronics generated substantially higher total and average revenue than the other categories.

### Fashion has the highest order volume

Fashion recorded the highest number of orders, demonstrating that order volume does not necessarily translate into the highest revenue.

### South is the strongest region

South generated the highest regional revenue and provides useful insights for regional sales planning.

### Quantity is not the only revenue driver

The weak positive Quantity–Revenue correlation indicates that product value, pricing, and transaction mix are also important factors.

### Outliers require validation

Extreme Quantity and Revenue values should be investigated before being classified as data-quality errors.

---

## 🚀 Business Recommendations

Based on the analysis:

* Investigate Electronics products responsible for high revenue per order.
* Study Fashion customers and products to understand how high order volume can be converted into higher order value.
* Review successful South-region sales patterns and consider applying them to other regions.
* Segment revenue by product, discount, customer type, and region for deeper analysis.
* Validate extreme Quantity and Revenue observations before removing them.

---

## ▶️ How to Run the Project

### 1. Install Pandas

```bash
pip install pandas
```

### 2. Keep the Files in the Same Folder

```text
Task_2/
├── task2_analysis.py
├── dataset.csv
├── BONUS REPORT.pdf
└── README.md
```

### 3. Run the Python Script

```bash
python task2_analysis.py
```

## The script will perform dataset inspection, descriptive analysis, category and regional analysis, revenue analysis, outlier checks, and correlation analysis.

## 📄 Bonus Report

The **`BONUS REPORT.pdf`** file provides a detailed summary of the project, including:

* Objective
* Dataset overview
* Analysis approach
* Key findings
* Revenue analysis
* Regional analysis
* Outlier analysis
* Correlation analysis
* Business interpretation
* Recommendations
* Conclusion

The report accompanies the Python/Pandas Task 2 project.

---

## 🏁 Conclusion

The analysis demonstrates a clear difference between **sales volume and revenue performance**.

Fashion generated the most orders, while Electronics generated the highest total and average revenue. South was the strongest regional contributor. The weak Quantity–Revenue correlation indicates that quantity alone is not sufficient to explain revenue performance; product pricing and transaction mix are also important.

Overall, this project demonstrates how **Python and Pandas can be used to transform raw e-commerce data into practical business insights** through descriptive statistics, grouping, outlier analysis, and correlation analysis.

---

## 👨‍💻 Internship Details

**Organization:** CODSOFT
**Task:** Task 2 – E-Commerce Sales Analysis
**Technology:** Python & Pandas
**Dataset Size:** 1,000 Orders
**Status:** Completed ✅

---

## 📌 Skills Demonstrated

* Python
* Pandas
* Data Analysis
* Descriptive Statistics
* Data Exploration
* GroupBy Analysis
* Revenue Analysis
* Outlier Analysis
* Correlation Analysis
* Business Insights
* Data-driven Recommendations

---

⭐ **This project is part of my CODSOFT Internship task submissions.**

