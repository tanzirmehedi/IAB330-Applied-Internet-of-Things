import time
import board
import busio
import adafruit_adxl34x
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create I2C bus and ADXL343 sensor object
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_adxl34x.ADXL343(i2c)

# Lists to store acceleration values
x_vals = []
y_vals = []
z_vals = []
time_vals = []

# Variable to track total elapsed time
total_time = 0.0

# Initialize plot
plt.figure()
plt.title("Real-Time Acceleration Data")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s^2)")

# Real-time plotting function
def update(frame):
    global total_time

    x, y, z = sensor.acceleration
    
    x_vals.append(x)
    y_vals.append(y)
    z_vals.append(z)
    time_vals.append(total_time)
    
    total_time += 0.05  # Increment total time by 0.1 seconds
    
    # Keep only the last 100 data points
    if len(time_vals) > 100:
        x_vals.pop(0)
        y_vals.pop(0)
        z_vals.pop(0)
        time_vals.pop(0)

    # Clear and update the plot
    plt.clf()
    plt.plot(time_vals, x_vals, label='X-axis', color='r')
    plt.plot(time_vals, y_vals, label='Y-axis', color='g')
    plt.plot(time_vals, z_vals, label='Z-axis', color='b')

    plt.title("Real-Time Acceleration Data")
    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (m/s^2)")
    plt.legend(loc='upper right')
    plt.grid(True)

# Create the animation
ani = FuncAnimation(plt.gcf(), update, interval=50)  # 50ms update interval

# Show plot
plt.show()