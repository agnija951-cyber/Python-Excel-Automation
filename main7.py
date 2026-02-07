import matplotlib.pyplot as plt
import pandas as pd

# 1. Data in English
data = {
    'Product': ['Laptops', 'Phones', 'Monitors', 'Headsets', 'Mice'],
    'Sales_EUR': [12000, 8500, 4300, 1500, 600]
}
df = pd.DataFrame(data)

# 2. Create a figure with two subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Annual Sales Performance Analysis', fontsize=16, fontweight='bold')

# --- Chart 1: Bar Chart ---
ax1.bar(df['Product'], df['Sales_EUR'], color='#4F81BD')
ax1.set_title('Sales Revenue by Product')
ax1.set_ylabel('Revenue (EUR)')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# --- Chart 2: Pie Chart ---
ax2.pie(df['Sales_EUR'], labels=df['Product'], autopct='%1.1f%%', 
        startangle=140, colors=['#4F81BD', '#C0504D', '#9BBB59', '#8064A2', '#4BACC6'])
ax2.set_title('Market Share Distribution')

# Adjust layout to prevent overlapping
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# 3. Save as PDF
plt.savefig("Professional_Visual_Analytics.pdf", bbox_inches='tight', dpi=300)
print("English Charts PDF created successfully!")