# pandas
# pandas is used for data manipulation and analysis, especially with tabular data.

# Example: Basic Operations with pandas

import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)

# Display basic statistics
print("DataFrame:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

print("\nMean Age:")
print(df['Age'].mean())
