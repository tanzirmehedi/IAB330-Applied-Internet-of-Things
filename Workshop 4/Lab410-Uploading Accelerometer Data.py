import time
from datetime import datetime
import board
import busio
import adafruit_adxl34x
from pymongo import MongoClient

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_adxl34x.ADXL343(i2c)

uri = "mongodb+srv://stanzir:eJV3aC9SvSuI3E5P@cluster0.szzqnxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["HAR_db"]
data = db["acce_data"]

to_insert = []
for i in range(0, 20):
    x, y, z = sensor.acceleration
    document = {"measured_at": datetime.now(), "data": [x, y, z], "label": "Test"}
    to_insert.append(document)
    time.sleep(0.05)

data.insert_many(to_insert)