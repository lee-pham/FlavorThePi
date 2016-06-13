from sense_hat import SenseHat
import time
sense = SenseHat()
sense.clear()

while True:
    x, y, z = sense.get_accelerometer_raw().values()
    time.sleep(1)
    x2, y2, z2 = sense.get_accelerometer_raw().values()
    x, y, z = x2 - x, y2 - y, z2 - z
    mag = (x ** 2 + y ** 2 + z ** 2) ** 0.5
    print(mag),

sense.clear()
