import pyfirmata
import time

# This is for a windows machine that connected the Arduino to COM4
# In the Arduino IDE under Tools>Port you can look what port your Ardunio
# is connected to.
board = pyfirmata.Arduino('COM4')


it = pyfirmata.util.Iterator(board)
it.start()

#Define the pins
analog_input = board.get_pin('a:0:i')
led = board.get_pin('d:13:o')

while True:
    analog_value = analog_input.read()
    if analog_value is not None:
        delay = analog_value + 0.01
        led.write(1)
        time.sleep(delay)
        led.write(0)
        time.sleep(delay)
    else:
        time.sleep(0.1)