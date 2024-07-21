from gpiozero import Button
from signal import pause

# Define the button connected to GPIO18
button = Button(18)

def button_pressed():
    print("Button was pressed!")

# Assign the function to be called when the button is pressed
button.when_pressed = button_pressed

# Keep the program running to listen for button presses
pause()
