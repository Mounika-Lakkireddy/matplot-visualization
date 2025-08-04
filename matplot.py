import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel("Electronics_Sales_Data.xlsx")  # Adjust path if needed

# Bar Chart: Units Sold per Product
plt.figure(figsize=(8, 5))
plt.bar(df['Product'], df['Units Sold'], color='skyblue')
plt.title('Units Sold by Product')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.tight_layout()
plt.savefig('units_sold_bar_chart.png')
plt.show()

# Pie Chart: Revenue Share per Product
plt.figure(figsize=(7, 7))
plt.pie(df['Revenue ($)'], labels=df['Product'], autopct='%1.1f%%', startangle=140)
plt.title('Revenue Share by Product')
plt.tight_layout()
plt.savefig('revenue_share_pie_chart.png')
plt.show()

# Line Chart: Customer Ratings
plt.figure(figsize=(8, 5))
plt.plot(df['Product'], df['Customer Ratings'], marker='o', linestyle='-', color='green')
plt.title('Customer Ratings by Product')
plt.xlabel('Product')
plt.ylabel('Rating')
plt.ylim(3.5, 5)
plt.tight_layout()
plt.savefig('customer_ratings_line_chart.png')
plt.show()
