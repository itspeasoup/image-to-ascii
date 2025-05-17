# ascii image converter by peasoup
# Copyright (C) 2025 peasoup
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
# See <https://www.gnu.org/licenses/> for details.

import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk, ImageGrab
import pyperclip
import os

def open_image(event=None):
    file = filedialog.askopenfilename(filetypes=[
        ("images", "*.jpg;*.jpeg;*.png;*.gif;*.bmp;*.webp"),
        ("jpeg", "*.jpg"),
        ("png", "*.png"),
        ("gif", "*.gif"),
        ("bmp", "*.bmp"),
        ("webp", "*.webp")
    ])
    if file:
        load_and_convert(file)

def load_and_convert(path):
    global gimage
    gimage = Image.open(path).convert("RGBA")
    gimage.thumbnail((200, 200))
    img_label.image = ImageTk.PhotoImage(gimage)
    img_label.config(image=img_label.image)
    convert_to_ascii(gimage)

def convert_to_ascii(image):
    text_size = int(text_size_entry.get())

    width, height = image.size
    aspect_ratio = height / width
    new_width = text_size
    new_height = int(aspect_ratio * text_size * 0.5)

    resized = image.resize((new_width, new_height)).convert("RGBA")

    ascii_chars = ' .`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$⣿'
    ascii_chars = ascii_chars[::-1]

    ascii_image = ''
    for y in range(new_height):
        for x in range(new_width):
            r, g, b, a = resized.getpixel((x, y))
            if a == 0:
                ascii_image += ' '
            else:
                gray = int(0.299*r + 0.587*g + 0.114*b)
                ascii_image += ascii_chars[int(gray / 255 * (len(ascii_chars) - 1))]
        ascii_image += '\n'

    ascii_text.config(font=("Source Code Pro", 4))
    ascii_text.delete('1.0', tk.END)
    ascii_text.insert(tk.END, ascii_image)

def on_text_size_change(event):
    if gimage:
        convert_to_ascii(gimage)

def on_drop(event):
    file_path = event.data.strip('{}')  # handles paths with spaces
    if os.path.isfile(file_path):
        load_and_convert(file_path)

def on_paste(event=None):
    try:
        img = ImageGrab.grabclipboard()
        if isinstance(img, Image.Image):
            global gimage
            gimage = img.convert("RGBA")
            gimage.thumbnail((200, 200))
            img_label.image = ImageTk.PhotoImage(gimage)
            img_label.config(image=img_label.image)
            load_and_convert(gimage)
    except Exception as e:
        print("paste failed:", e)

def save_ascii():
    content = ascii_text.get("1.0", tk.END)
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt")])
    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)

def copy_ascii():
    content = ascii_text.get("1.0", tk.END)
    pyperclip.copy(content)

# GUI
root = TkinterDnD.Tk()
root.title("image-to-ascii (by peasoup)")

gimage = None

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)
root.bind("<Control-v>", on_paste)

open_button = tk.Button(root, text="open image", command=open_image)
open_button.pack()

img_label = tk.Label(root)
img_label.pack()

text_size_frame = tk.Frame(root)
text_size_frame.pack()

text_size_label = tk.Label(text_size_frame, text="text size:")
text_size_label.pack(side=tk.LEFT)

text_size_entry = tk.Entry(text_size_frame)
text_size_entry.pack(side=tk.LEFT)
text_size_entry.insert(0, "100")
text_size_entry.bind("<Return>", on_text_size_change)

ascii_text = tk.Text(root, height=50, width=120, font=("Source Code Pro", 4))
ascii_text.pack()

action_frame = tk.Frame(root)
action_frame.pack()

save_button = tk.Button(action_frame, text="save ascii", command=save_ascii)
save_button.pack(side=tk.LEFT, padx=5)

copy_button = tk.Button(action_frame, text="copy ascii", command=copy_ascii)
copy_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
