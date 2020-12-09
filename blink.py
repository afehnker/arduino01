import pyfirmata
import time

# This is for a windows machine that connected the Arduino to COM4
# In the Arduino IDE under Tools>Port you can look what port your Ardunio
# is connected to.
board = pyfirmata.Arduino('COM4')

while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)

