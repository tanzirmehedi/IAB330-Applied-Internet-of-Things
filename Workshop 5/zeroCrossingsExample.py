import numpy as np
import matplotlib.pyplot as plt

def zero_crossing_rate(data):
    zero_crossings = np.where(np.diff(np.sign(data)))[0]
    zcr = len(zero_crossings)
    return zcr

# Generate example data (a simple sine wave with some noise)
time = np.linspace(0, 1, 500)  # 1 second of data at 500 Hz
frequency = 5  # 5 Hz sine wave
data = np.sin(2 * np.pi * frequency * time) + 0.5 * np.random.randn(time.size)

# Calculate the zero-crossing rate
zcr = zero_crossing_rate(data)

# Print the zero-crossing rate
print(f"Zero-Crossing Rate: {zcr}")

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(time, data, label="Signal")
plt.title("Signal with Zero-Crossings")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.axhline(0, color='black', lw=1, ls='--')
plt.legend()
plt.show()
