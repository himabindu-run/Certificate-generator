from PIL import Image, ImageDraw, ImageFont

import pandas as pd

data_form = pd.read_excel("file.xlsx")

name_list = data_form['Name'].to_list()

id_ = len(name_list)

for name, i in enumerate(name_list):
    im = Image.open("Template.png")
    d = ImageDraw.Draw(im)
    location = (0, 0)
    font_color = (230, 254, 255)
    font = ImageFont.truetype("Itim.ttf", 50, encoding = "unic")
    d.text(location, i.title(), fill = font_color,font = font)
    im.save("certificate_" + i + ".png")
    print("(%d/%d) Certificate Created for:  %s" % (name + 1, id_, i.title()))


