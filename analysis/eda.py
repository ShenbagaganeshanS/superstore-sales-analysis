import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('C:/Users/shenb/Desktop/data_analysis/Sales/Output/sample.csv')

# Set visual theme
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# -------------------------------
# 1. Sales and Profit by Region
region_summary = df.groupby('region')[['sales', 'profit']].sum().sort_values(by='sales', ascending=False)
region_summary.plot(kind='bar', title='Sales and Profit by Region')
plt.ylabel('Amount')
plt.tight_layout()
plt.savefig('C:/Users/shenb/Desktop/data_analysis/Sales/Output/sales_profit_by_region.png')
plt.clf()

# -------------------------------
# 2. Top 10 Sub-Categories by Profit
subcat_profit = df.groupby('sub-category')['profit'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=subcat_profit.values, y=subcat_profit.index, palette='viridis')
plt.title('Top 10 Sub-Categories by Profit')
plt.xlabel('Profit')
plt.tight_layout()
plt.savefig('C:/Users/shenb/Desktop/data_analysis/Sales/Output/top_subcategories_profit.png')
plt.clf()

# -------------------------------
# 3. Monthly Sales Trend
monthly_sales = df.groupby('order_month')['sales'].sum()
monthly_sales.plot(marker='o', title='Monthly Sales Trend')
plt.xticks(rotation=45)
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('C:/Users/shenb/Desktop/data_analysis/Sales/Output/monthly_sales_trend.png')
plt.clf()

# -------------------------------
# 4. Profit vs Sales (Scatter)
sns.scatterplot(data=df, x='sales', y='profit', hue='category')
plt.title('Profit vs Sales by Category')
plt.tight_layout()
plt.savefig('C:/Users/shenb/Desktop/data_analysis/Sales/Output/profit_vs_sales.png')
plt.clf()

# -------------------------------
# 5. Sales by Segment
segment_sales = df.groupby('segment')['sales'].sum()
segment_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales by Customer Segment')
plt.ylabel('')
plt.tight_layout()
plt.savefig('C:/Users/shenb/Desktop/data_analysis/Sales/Output/sales_by_segment.png')

print("✅ EDA complete. Visuals saved in Output folder.")
