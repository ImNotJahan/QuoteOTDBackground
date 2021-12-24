import requests
from PIL import Image, ImageFont, ImageDraw
import ctypes
import os

url = "http://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=5"
response = requests.get(url)
data = response.json()

quote = data["thought"]["quote"]
quote = quote.replace(',', ",\n")

array = quote.split()
quote = ''
for i in range(0, len(array), 7):
    quote += ' '.join(array[i:i+7]) + '\n'

BACKGROUND = Image.open("background.jpg")
USABLE_BACKGROUND = ImageDraw.Draw(BACKGROUND)

WIDTH, HEIGHT = BACKGROUND.size

FONT = ImageFont.truetype("CONSOLA.TTF", round(WIDTH / 45))

width, height = USABLE_BACKGROUND.textsize(quote, font=FONT)

USABLE_BACKGROUND.text(((WIDTH - width) / 2, (HEIGHT - height) / 2),
                       quote, (130, 130, 255), font=FONT, anchor="mm")
BACKGROUND.save("changed_background.jpg")
ctypes.windll.user32.SystemParametersInfoW(20, 0, 'D:\\changed_background.jpg', 0)
