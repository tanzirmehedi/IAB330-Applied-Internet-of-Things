import time
import csv
import board
import busio
import adafruit_adxl34x

# Initialize I2C bus and accelerometer
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_adxl34x.ADXL343(i2c)

# Open a CSV file to write data
with open('acceleration_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Milliseconds", "X", "Y", "Z"])

    start_time = time.time()

    while True:
        x, y, z = sensor.acceleration
        # Calculate elapsed time in milliseconds
        elapsed_time = (time.time() - start_time) * 1000
        writer.writerow([int(elapsed_time), f"{x:.2f}", f"{y:.2f}", f"{z:.2f}"])
        print(f"{int(elapsed_time)} ms -> X: {x:.2f}, Y: {y:.2f}, Z: {z:.2f}")
        time.sleep(0.2)
