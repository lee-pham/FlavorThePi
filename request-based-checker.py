from sense_hat import SenseHat
from twython import Twython
sense = SenseHat()
sense.clear()
app_key = 'appkey'
app_secret = 'appsecret'
access_token = 'accesstoken'
access_token_secret = 'accesstokensecret'
handle = Twython(app_key, app_secret, access_token, access_token_secret)
mention = handle.get_mentions_timeline(count=1)
for mentions in mention:
    color = mentions['text']
color = color[13:len(color)].lower()
if color == 'red':
    print('cherry')
    sense.clear([255, 0, 0])
elif color == 'orange':
    print('mango')
    sense.clear([255, 127, 0])
elif color == 'yellow':
    print('pineapple')
    sense.clear([255, 255, 0])
elif color == 'green':
    print('key lime')
    sense.clear([0, 255, 0])
elif color == 'blue':
    print('blueberry')
    sense.clear([0, 0, 255])
elif color == 'indigo':
    print('blackberry')
    sense.clear([75, 0, 130])
elif color == 'violet':
    print('passion fruit')
    sense.clear([127, 0, 255])
else:
    print("don't know that recipe!")
