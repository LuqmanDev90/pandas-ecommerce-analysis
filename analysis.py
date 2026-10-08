"""
E-Commerce Sales Data Analysis with Pandas
Complete beginner-friendly project
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================
# 1. DATA LOADING
# ============================================
print("=" * 60)
print("🛍️  E-COMMERCE SALES DATA ANALYSIS")
print("=" * 60)

# CSV file ko load karo
df = pd.read_csv('data/ecommerce_sales.csv')

print("\n📊 Dataset ka shape:", df.shape)
print("\n📋 Pehle 5 rows:")
print(df.head())

print("\n📝 Dataset info:")
print(df.info())

print("\n📈 Dataset ke statistics:")
print(df.describe())

# ============================================
# 2. DATA CLEANING
# ============================================
print("\n" + "=" * 60)
print("🧹 DATA CLEANING")
print("=" * 60)

# Missing values check karo
print("\n❓ Missing values:")
print(df.isnull().sum())

# Data types check karo
print("\nData Types:")
print(df.dtypes)

# ============================================
# 3. BASIC ANALYSIS
# ============================================
print("\n" + "=" * 60)
print("📊 BASIC ANALYSIS")
print("=" * 60)

print("\n💰 Total Sales:", f"₹{df['Sales'].sum():,.2f}")
print("💹 Total Profit:", f"₹{df['Profit'].sum():,.2f}")
print("📦 Total Orders:", df.shape[0])
print("🏷️  Total Products Sold:", df['Quantity'].sum())
print("📊 Average Order Value:", f"₹{df['Sales'].mean():,.2f}")

# ============================================
# 4. TOP PRODUCTS ANALYSIS
# ============================================
print("\n" + "=" * 60)
print("⭐ TOP 10 PRODUCTS BY SALES")
print("=" * 60)

top_products = df.groupby('Product_Name').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Quantity': 'sum',
    'Order_ID': 'count'  # Number of orders
}).sort_values('Sales', ascending=False).head(10)

top_products.columns = ['Total Sales', 'Total Profit', 'Quantity Sold', 'Orders']
print(top_products)

# ============================================
# 5. CATEGORY ANALYSIS
# ============================================
print("\n" + "=" * 60)
print("🏷️  CATEGORY-WISE ANALYSIS")
print("=" * 60)

category_analysis = df.groupby('Category').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Quantity': 'sum',
    'Order_ID': 'count'
}).sort_values('Sales', ascending=False)

category_analysis.columns = ['Total Sales', 'Total Profit', 'Quantity', 'Orders']
print(category_analysis)

# ============================================
# 6. REGION ANALYSIS
# ============================================
print("\n" + "=" * 60)
print("🗺️  REGION-WISE ANALYSIS")
print("=" * 60)

region_analysis = df.groupby('Region').agg({
    'Sales': ['sum', 'mean'],
    'Profit': ['sum', 'mean'],
    'Order_ID': 'count'
}).sort_values(('Sales', 'sum'), ascending=False)

print(region_analysis)

# Detailed region breakdown
print("\n📍 Region-wise Summary:")
for region in df['Region'].unique():
    region_data = df[df['Region'] == region]
    print(f"\n{region} Region:")
    print(f"  Total Sales: ₹{region_data['Sales'].sum():,.2f}")
    print(f"  Total Profit: ₹{region_data['Profit'].sum():,.2f}")
    print(f"  Number of Orders: {len(region_data)}")
    print(f"  Profit Margin: {(region_data['Profit'].sum() / region_data['Sales'].sum() * 100):.2f}%")

# ============================================
# 7. DISCOUNT ANALYSIS
# ============================================
print("\n" + "=" * 60)
print("🏷️  DISCOUNT ANALYSIS")
print("=" * 60)

print("\nDiscount Distribution:")
print(f"No Discount: {len(df[df['Discount'] == 0])} orders")
print(f"5% Discount: {len(df[df['Discount'] == 0.05])} orders")
print(f"10% Discount: {len(df[df['Discount'] == 0.10])} orders")
print(f"15% Discount: {len(df[df['Discount'] == 0.15])} orders")
print(f"20%+ Discount: {len(df[df['Discount'] >= 0.20])} orders")

# Impact of discount on profit
avg_profit_with_discount = df[df['Discount'] > 0]['Profit'].mean()
avg_profit_no_discount = df[df['Discount'] == 0]['Profit'].mean()

print(f"\nAverage Profit (With Discount): ₹{avg_profit_with_discount:,.2f}")
print(f"Average Profit (No Discount): ₹{avg_profit_no_discount:,.2f}")

# ============================================
# 8. CUSTOMER ANALYSIS
# ============================================
print("\n" + "=" * 60)
print("👥 CUSTOMER ANALYSIS")
print("=" * 60)

print(f"\nTotal Unique Customers: {df['Customer_ID'].nunique()}")

customer_stats = df.groupby('Customer_ID').agg({
    'Order_ID': 'count',
    'Sales': 'sum',
    'Profit': 'sum'
}).sort_values('Sales', ascending=False)

customer_stats.columns = ['Orders', 'Total Spent', 'Total Profit']
print("\nTop 10 Customers:")
print(customer_stats.head(10))

# ============================================
# 9. VISUALIZATIONS
# ============================================
print("\n" + "=" * 60)
print("📈 CREATING VISUALIZATIONS...")
print("=" * 60)

# Set style
sns.set_style("whitegrid")
plt.figure(figsize=(16, 12))

# 1. Category-wise Sales
plt.subplot(2, 3, 1)
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
category_sales.plot(kind='bar', color=['#FF6B6B', '#4ECDC4'], ax=plt.gca())
plt.title('Category-wise Sales', fontsize=12, fontweight='bold')
plt.ylabel('Sales (₹)')
plt.xticks(rotation=0)
plt.grid(axis='y')

# 2. Region-wise Sales
plt.subplot(2, 3, 2)
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
region_sales.plot(kind='bar', color=['#95E1D3', '#F38181', '#AA96DA', '#FCBAD3'], ax=plt.gca())
plt.title('Region-wise Sales', fontsize=12, fontweight='bold')
plt.ylabel('Sales (₹)')
plt.xticks(rotation=0)
plt.grid(axis='y')

# 3. Top 10 Products
plt.subplot(2, 3, 3)
top_10_products = df.groupby('Product_Name')['Sales'].sum().sort_values(ascending=False).head(10)
top_10_products.plot(kind='barh', color='#A8E6CF', ax=plt.gca())
plt.title('Top 10 Products by Sales', fontsize=12, fontweight='bold')
plt.xlabel('Sales (₹)')
plt.tight_layout()

# 4. Profit vs Sales Scatter
plt.subplot(2, 3, 4)
plt.scatter(df['Sales'], df['Profit'], alpha=0.6, s=100, color='#FF6B9D')
plt.title('Profit vs Sales', fontsize=12, fontweight='bold')
plt.xlabel('Sales (₹)')
plt.ylabel('Profit (₹)')
plt.grid(True, alpha=0.3)

# 5. Discount Distribution
plt.subplot(2, 3, 5)
discount_counts = df['Discount'].value_counts().sort_index()
discount_counts.plot(kind='bar', color='#FEC8D8', ax=plt.gca())
plt.title('Discount Distribution', fontsize=12, fontweight='bold')
plt.ylabel('Number of Orders')
plt.xlabel('Discount (%)')
plt.xticks(rotation=0)
plt.grid(axis='y')

# 6. Category-wise Profit
plt.subplot(2, 3, 6)
category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
colors = ['#C1FFD7', '#C1D7FF']
category_profit.plot(kind='pie', autopct='%1.1f%%', colors=colors, ax=plt.gca())
plt.title('Category-wise Profit Distribution', fontsize=12, fontweight='bold')
plt.ylabel('')

plt.tight_layout()
plt.savefig('analysis_results.png', dpi=300, bbox_inches='tight')
print("✅ Charts saved as 'analysis_results.png'")
plt.show()

# ============================================
# 10. KEY INSIGHTS
# ============================================
print("\n" + "=" * 60)
print("💡 KEY INSIGHTS & RECOMMENDATIONS")
print("=" * 60)

# Best performing category
best_category = df.groupby('Category')['Profit'].sum().idxmax()
print(f"\n✅ Best Performing Category: {best_category}")

# Best performing region
best_region = df.groupby('Region')['Sales'].sum().idxmax()
print(f"✅ Best Performing Region: {best_region}")

# Best selling product
best_product = df.groupby('Product_Name')['Sales'].sum().idxmax()
print(f"✅ Best Selling Product: {best_product}")

# Profit Margin
profit_margin = (df['Profit'].sum() / df['Sales'].sum()) * 100
print(f"✅ Overall Profit Margin: {profit_margin:.2f}%")

# High discount impact
high_discount = df[df['Discount'] >= 0.20]
low_discount = df[df['Discount'] < 0.10]
print(f"\n⚠️  High Discount (20%+) Orders: {len(high_discount)}")
print(f"   Average Profit: ₹{high_discount['Profit'].mean():,.2f}")
print(f"\n✅ Low Discount (<10%) Orders: {len(low_discount)}")
print(f"   Average Profit: ₹{low_discount['Profit'].mean():,.2f}")

print("\n" + "=" * 60)
print("✨ Analysis Complete! Check 'analysis_results.png' for charts")
print("=" * 60)
