from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

for i in range(0, 10):
    sense.show_letter(str(i))

sense.clear()
