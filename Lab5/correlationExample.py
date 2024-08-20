import numpy as np

# Example data
a = [0.1, 0.3, 0.5, 0.7, 0.9]
b = [0.2, 0.4, 0.6, 0.8, 1.0]
c = [0.1, -0.3, 0.5, -0.2, 0.0]

# Calculate the correlation matrix
data = np.array([a, b, c])

correlation_matrix = np.corrcoef(data)

print("Correlation matrix:\n", correlation_matrix)