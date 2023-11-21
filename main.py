# pip install Pillow
import sys
from PIl import Image, ImageDraw, ImageFont, ImageFilter, ImageTk
from tkinter import *


root = tk.TK()
root.geometry('1000x600')
root.title('Photo Editor')
root.config(bg=blue)

pen = 'red'
pen = 5
file_path = ""

lframe = tk.frame(root, width=200, height=600, bg='skyblue')
lframe.pack(side='left', fill='y') 



message = input('Enter your Text here')

image = with Image.open('<file name>').convert('RGBA') as base:


    text = Image.new('RGBA', base.szie, (255, 255, 255, 0))

    font = ImageFont.truetype('pillow/Test/fonts/FreeMono..ttf', 40)

    d = ImageDraw.Draw(txt)

    d.text((10, 10)), message, font=ft, fill=(255, 255, 255, 128))

    d.text((10, 60)), message, font=ft, fill=(255, 255, 255, 255))

    out = Image.alpha_composite(base, txt)

# save the image
    image.save('<file name>')

# make it look more detail
    image.filter(ImageFilter).Shoot()).show()


    out.show()


root.mainloop()
