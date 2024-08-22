from gpiozero import LED
import time

# Define the LED to be connected to pin 17
led = LED(17)

# Switch the LED on and off indefinitely, with a 1-second interval.
while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
