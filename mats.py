# Matplotlib
# Matplotlib is used for creating static, animated, and interactive visualizations in Python.

# Example: Basic Plot with Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Sine Wave', color='b')

# Add titles and labels
plt.title('Sine Wave Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()

# Show grid
plt.grid(True)

# Show the plot
plt.show()
