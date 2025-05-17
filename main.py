import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk
import pyperclip  # for clipboard support

def open_image(event=None):
    global image_path, gimage
    image_path = filedialog.askopenfilename(filetypes=[
        ("Images", "*.jpg;*.jpeg;*.png;*.gif;*.bmp;*.webp"),
        ("JPEG (mspaint quality - transparency)", "*.jpg"),
        ("PNG (good quality + transparency)", "*.png"),
        ("GIF (text won't be animated)", "*.gif"),
        ("BMP (raster/bitmap) - transparency", "*.bmp"),
        ("WEBP (from google images / discord + transparency)", "*.webp")
    ])
    if image_path:
        gimage = Image.open(image_path)
        gimage.thumbnail((200, 200))  # adjust the size for display
        img_label.image = ImageTk.PhotoImage(gimage)
        img_label.config(image=img_label.image)
        convert_to_ascii(gimage)

def convert_to_ascii(image):
    text_size = int(text_size_entry.get())

    width, height = image.size
    aspect_ratio = height / width
    new_width = text_size
    new_height = int(aspect_ratio * text_size * 0.55)

    resized_image = image.resize((new_width, new_height))
    grayscale_image = resized_image.convert('L')

    ascii_chars = '█▓▒░@%#*+=-:. '  # Add more characters for more variation

    ascii_image = ''
    for y in range(new_height):
        for x in range(new_width):
            pixel_value = grayscale_image.getpixel((x, y))
            if pixel_value == 0:
                ascii_image += ' '
            else:
                ascii_image += ascii_chars[int(pixel_value / 255 * (len(ascii_chars) - 1))]
        ascii_image += '\n'

    ascii_text.config(font=("Courier New", 8))
    ascii_text.delete('1.0', tk.END)
    ascii_text.insert(tk.END, ascii_image)

def on_text_size_change(event):
    convert_to_ascii(gimage)

def on_drop(event):
    """Handle files dropped into the window"""
    file_path = event.data
    if file_path:
        global image_path, gimage
        image_path = file_path[0]
        gimage = Image.open(image_path)
        gimage.thumbnail((200, 200))  # adjust the size for display
        img_label.image = ImageTk.PhotoImage(gimage)
        img_label.config(image=img_label.image)
        convert_to_ascii(gimage)

def on_paste(event=None):
    """Handle pasting image data from clipboard"""
    try:
        image_data = root.clipboard_get()
        if image_data:
            global image_path, gimage
            gimage = Image.open(image_data)
            gimage.thumbnail((200, 200))  # adjust the size for display
            img_label.image = ImageTk.PhotoImage(gimage)
            img_label.config(image=img_label.image)
            convert_to_ascii(gimage)
    except:
        pass

# GUI
root = TkinterDnD.Tk()
root.title("image-to-ascii (by peasoup)")

image_path = ""
gimage = None

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

img_label = tk.Label(root)
img_label.pack()

text_size_frame = tk.Frame(root)
text_size_frame.pack()

text_size_label = tk.Label(text_size_frame, text="Text Size:")
text_size_label.pack(side=tk.LEFT)

text_size_entry = tk.Entry(text_size_frame)
text_size_entry.pack(side=tk.LEFT)
text_size_entry.insert(0, "100")
text_size_entry.bind("<Return>", on_text_size_change)

ascii_text = tk.Text(root, height=30, width=60, font=("Courier New", 4))
ascii_text.pack()

# Bind paste event to handle clipboard paste
root.bind("<Control-v>", on_paste)

root.mainloop()
