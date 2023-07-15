import os
import qrcode

# Add the link of the website 
img = qrcode.make("https://clickcristiano.com/")

img.save("qr.png", "PNG")

os.system("display qr.png")

