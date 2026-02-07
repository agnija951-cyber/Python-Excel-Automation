import matplotlib.pyplot as plt
import pandas as pd

# 1. Data with English headers and values
data = [
    ['New York', 12000, 10000],
    ['London', 8500, 9000],
    ['Tokyo', 15000, 12000],
    ['Berlin', 5000, 8000]
]

df = pd.DataFrame(data, columns=['City', 'Sales', 'Target'])

# 2. Logic for Status
def get_status(row):
    if row['Sales'] > row['Target']:
        return 'EXCEEDED'
    elif row['Sales'] == row['Target']:
        return 'REACHED'
    else:
        return 'BELOW TARGET'

df['Status'] = df.apply(get_status, axis=1)

# 3. Create the table
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# 4. Professional Styling
for i in range(len(df)):
    sales = df.iloc[i, 1]
    target = df.iloc[i, 2]
    
    if sales > target:
        table[(i+1, 3)].set_facecolor("#90ee90") # Green
    elif sales < target:
        table[(i+1, 3)].set_facecolor("#ffcccb") # Red

table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 2)

# 5. Save as PDF
plt.savefig("Professional_Sales_Report.pdf", bbox_inches='tight', dpi=300)
print("English PDF report created successfully!")