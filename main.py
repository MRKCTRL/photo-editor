# pip install Pillow
import sys
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageTk, 
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

root = tk.Tk()
root.geometry('1000x600')
root.title('Photo Editor')
root.config(bg='blue')

pen_c = 'red'
pen_s = 5
file_path = ""

def add_img():
    global file_path
    file_path = filedialog.askopenfile(initialdir='/home/jabu/Pictures/')
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.ANTIALIAS)
    canvas.config(width=image.width, height = image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image 
    canvas.create_image(0, 0, image=image, anchor='nw')
    
    
filter_label = tk.label(lframe, text='choose filter', bg='black')
filter_label.pack()
filterComboBox = ttk.Combobox(lframe, values=['Black and white', 'Blur', 'Emboss', 'Sharpen', 'smooth'])
filterComboBox.pack()

filterComboBox.bind('<<ComboboxSelected>>', lambda event: apply_filter(filterComboBox.get()))

lframe = tk.frame(root, width=200, height=600, bg='skyblue')
lframe.pack(side='left', fill='y') 

canvas = tk.Canvas(root, width=800, height=650)
canvas.pack

img_button = tk.Button(lframe, text='Add img', bg='navy')
img_button.pack(pady=12)

colorOfButtun = tk.Button(lframe,text='Change Pencil color', command=change_color,bg='green')
colorOfButtun.pack(pady=6)

pen_size_frame = tk.Frame(lframe, bg='yellow')
pen_size_frame.pack(pady=4)

pen_size_s = tk.Radiobutton(pen, text='Small', command=lambda: change_size(3), value=3, bg='lime')
pen_size_s.pack(side='left')

pen_size_m = tk.Radiobutton(pen, text='Meduim', value=6, command=lambda: change_size(6), bg='lime')
pen_size_m.pack(side='left')
pen_size_m.select()

pen_size_l = tk.Radiobutton(pen, text='Larg',command=lambda: change_size(9), value=9, bg='lime')
pen_size_l.pack(side='left')

erase_button = tk.Button(lframe, text='erase', command=clear_canvas, bg='#FF9797')
erase_button.pack(pady=10)

def change_size(size):
    global pen_s
    pen_s = size

def change_color():
    global pen_c
    pen_c = colorchooser.askcolor(title='Select Pen Color')[1]

def write(event):
    x1, y1 = (event.x - pen), (event.y - pen)
    x2, y2 = (event.x + pen), (event.y + pen)
    canvas.create_oval(x1,y1,x2,y2, fill=pen_c, outline='')
    
def clear_canvas():
    canvas.delete('all') 
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')
    
    
def apply_filter(filter):
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.ANTIALIAS)
    if filter == 'Black and white':
        image = ImageOps.grayscale(image)
    elif filter == 'Blur':
        image = image.filter(ImageFilter.BLUR)
    elif filter == 'Sharpen':
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == 'Smooth':
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == 'Emboss':
        image = image.filter(ImageFilter.EMBOSS)
        


canvas.bind('<B1-Motion>', write)



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
