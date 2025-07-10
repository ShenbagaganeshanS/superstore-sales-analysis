# analysis/superstore_analysis.py

import pandas as pd

# Load dataset
df = pd.read_csv('C:/Users/shenb/Desktop/data_analysis/Sales/data/Superstore.csv', encoding='ISO-8859-1')


# Rename columns for consistency
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# Convert dates
df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])

# Drop duplicates
df.drop_duplicates(inplace=True)

# Optional: Add calculated fields
df['order_month'] = df['order_date'].dt.to_period('M')
df['profit_margin'] = df['profit'] / df['sales']

# Save cleaned version for Power BI
df.to_csv('C:/Users/shenb/Desktop/data_analysis/Sales/Output/sample.csv', index=False)
print("✅ Data cleaned and exported to output/clean_superstore.csv")
