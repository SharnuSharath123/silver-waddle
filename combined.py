# Combining NumPy, pandas, and Matplotlib
# Here’s a more comprehensive example that combines all three libraries to analyze and visualize some data:

# Example: Data Analysis and Visualization

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(0)
dates = pd.date_range(start='2023-01-01', periods=12, freq='M')
sales = np.random.randint(1000, 5000, size=len(dates))

# Create a DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Sales': sales
})

# Basic Data Analysis
mean_sales = df['Sales'].mean()
median_sales = df['Sales'].median()
max_sales = df['Sales'].max()
min_sales = df['Sales'].min()

print("Basic Data Analysis:")
print(f"Mean Sales: ${mean_sales:.2f}")
print(f"Median Sales: ${median_sales:.2f}")
print(f"Maximum Sales: ${max_sales:.2f}")
print(f"Minimum Sales: ${min_sales:.2f}")

# Data Visualization
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Sales'], marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Data')
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
