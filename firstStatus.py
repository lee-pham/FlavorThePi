from twython import Twython
app_key = 'appkey'
app_secret = 'appsecret'
access_token = 'accesstoken'
access_token_secret = 'accesstokensecret'
handle = Twython(app_key, app_secret, access_token, access_token_secret)
handle.update_status(status = "Breathing a twitter bot's first breaths @UTCompSci's MAD Hack Night w/ @google")
