#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('sales_data.csv')

# Clean column names
df.columns = df.columns.str.strip()

# Convert necessary columns to numeric
df['Quantity Sold'] = pd.to_numeric(df['Quantity Sold'], errors='coerce')
df['Revenue ($)'] = pd.to_numeric(df['Revenue ($)'], errors='coerce')

# Analysis
total_revenue = df['Revenue ($)'].sum()
product_sales = df.groupby('Product')['Quantity Sold'].sum()
best_selling_product = product_sales.idxmax()
best_selling_quantity = product_sales.max()

daily_sales = df.groupby('Date')['Revenue ($)'].sum()
highest_sales_day = daily_sales.idxmax()
highest_sales_value = daily_sales.max()

# Save summary
with open('sales_summary.txt', 'w') as file:
    file.write(f"Total Revenue: ${total_revenue:,}\n")
    file.write(f"Best-Selling Product: {best_selling_product} ({best_selling_quantity} units sold)\n")
    file.write(f"Highest Sales Day: {highest_sales_day} (${highest_sales_value:,})\n")

# Print summary
print("📊 Sales Insights:")
print(f"➡️ Total Revenue: ${total_revenue:,}")
print(f"➡️ Best-Selling Product: {best_selling_product} ({best_selling_quantity} units sold)")
print(f"➡️ Highest Sales Day: {highest_sales_day} (${highest_sales_value:,})")

# Plot
plt.figure(figsize=(10, 5))
daily_sales.plot(kind='line', marker='o', title='Daily Revenue Trend')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.grid(True)
plt.tight_layout()
plt.savefig('daily_revenue_trend.png')
plt.show()
