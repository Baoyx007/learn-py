__author__ = 'haven'
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('arial.ttf', 36)
draw = ImageDraw.Draw(image)


def rnd_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rnd_color())


def rnd_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def rnd_char():
    return chr(random.randint(65, 90))


for t in range(4):
    draw.text((60 * t + 10, 10), rnd_char(), font=font, fill=rnd_color2())

image = image.filter(ImageFilter.BLUR)

image.save('veri_code.jpg', 'jpeg')
