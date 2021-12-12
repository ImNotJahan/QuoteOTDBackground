import requests
from PIL import Image, ImageFont, ImageDraw

url = "http://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=5"
response = requests.get(url)
data = response.json()

quote = data["thought"]["quote"]
quote = quote.replace(',', ",\n")
print(quote)

BACKGROUND = Image.open("background.jpeg")
FONT = ImageFont.truetype("CONSOLA.TTF", 12)
USABLE_BACKGROUND = ImageDraw.Draw(BACKGROUND)

USABLE_BACKGROUND.text((15,15), quote, (0, 0, 0), font=FONT)

BACKGROUND.save("changed_background.jpeg")
