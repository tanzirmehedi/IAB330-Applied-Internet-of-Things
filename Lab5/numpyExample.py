import numpy as np

# Example values
data = [3, 7, 2, 9, 4]

# Calculate the range as the difference between max and min
range_value = np.max(data) - np.min(data)

print("Range:", range_value) # Range: 6