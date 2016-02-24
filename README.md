# FlavorThePi
Control the Raspberry Pi Sense Hat via mentions to [@flavorthepi](https://twitter.com/flavorthepi)

Tweet '@flavorthepi [a Roy G. Biv color]' and an attached LED matrix will change to the corresponding request.
  example: ```@flavorthepi orange```

Alternatively, tweet '@flavorthepi flash [message]' and your message will begin to scroll on the matrix.
  example: ```@flavorthepi flash scrolling message!```
  
All possible with the help of the [Twython](https://github.com/ryanmcgrath/twython) Python library that allows for access to Twitter data.
