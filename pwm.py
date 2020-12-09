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
led = board.get_pin('d:11:p')

while True:
    analog_value = analog_input.read()
    if analog_value is not None:
        led.write(analog_value)
    time.sleep(0.1)