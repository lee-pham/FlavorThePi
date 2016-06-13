from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
    x, y, z = sense.get_accelerometer_raw().values()
    mag = (x ** 2 + y ** 2 + z ** 2) ** 0.5
    print(mag),

sense.clear()
