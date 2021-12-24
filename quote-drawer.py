import requests
from PIL import Image, ImageFont, ImageDraw
import ctypes
import os

url = "http://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=5"
response = requests.get(url)
data = response.json()

quote = data["thought"]["quote"]
quote = quote.replace(',', ",\n")

BACKGROUND = Image.open("background.jpg")
FONT = ImageFont.truetype("CONSOLA.TTF", 70)
USABLE_BACKGROUND = ImageDraw.Draw(BACKGROUND)

WIDTH, HEIGHT = BACKGROUND.size

USABLE_BACKGROUND.text((WIDTH / 2, HEIGHT / 2), quote, (255, 255, 255), font=FONT, anchor="mm")

BACKGROUND.save("changed_background.jpg")
ctypes.windll.user32.SystemParametersInfoW(20, 0, 'D:\\changed_background.jpg', 0)
