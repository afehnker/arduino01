import pyfirmata
import time

# This is for a windows machine that connected the Arduino to COM4
# In the Arduino IDE under Tools>Port you can look what port your Ardunio
# is connected to.
board = pyfirmata.Arduino('COM4')


it = pyfirmata.util.Iterator(board)
it.start()

#Define the pins
digital_input = board.get_pin('d:10:i')
led = board.get_pin('d:13:o')

while True:
    sw = digital_input.read()
    if sw is True:
        led.write(1)
    else:
        led.write(0)
    time.sleep(0.1)