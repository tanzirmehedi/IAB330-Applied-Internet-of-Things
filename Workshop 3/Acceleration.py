import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_adxl34x.ADXL343(i2c)

while True:
    x, y, z = sensor.acceleration
    print(f"{x:.2f}, {y:.2f}, {z:.2f}")
    time.sleep(0.2)
