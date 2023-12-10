import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    global image_path, gimage
    image_path = filedialog.askopenfilename(filetypes=[("images", "*.jpg;*.jpeg;*.png;*.gif;*.bmp;*.webp"),("jpeg (microsoft paint quality)","*.jpg"),("png (good quality + transparency)","*.png"),("gif (text won't be animated)","*.gif"),("bmp (raster/bitmap)","*.bmp"),("webp (the one you downloaded from google images or discord probably + transparency)","*.webp")])
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
    new_height = int(aspect_ratio * text_size * 0.5)

    resized_image = image.resize((new_width, new_height))
    grayscale_image = resized_image.convert('L')

    ascii_chars = '█@&%#*░+=-:,.\/|][}{)(´„‟‚‛‘ '  # add more characters if you want

    ascii_image = ''
    for y in range(new_height):
        for x in range(new_width):
            pixel_value = grayscale_image.getpixel((x, y))
            if pixel_value == 255:  # make sure to use the GOD DAM transparency
                ascii_image += ' '
            else:
                ascii_image += ascii_chars[int(pixel_value / 255 * (len(ascii_chars) - 1))]
        ascii_image += '\n'

    ascii_text.config(font=("Courier New", 8))  # set the font to "Courier New"
    ascii_text.delete('1.0', tk.END)
    ascii_text.insert(tk.END, ascii_image)



def on_text_size_change(event):
    convert_to_ascii(gimage)

# GUI
root = tk.Tk()
root.title("image-to-ascii (by peasoup)")

image_path = ""
gimage = None

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
text_size_entry.insert(0, "100")  # that's the default text size
text_size_entry.bind("<Return>", on_text_size_change)

ascii_text = tk.Text(root, height=20, width=50, font=("Courier New", 8))  # set the font
ascii_text.pack()

root.mainloop()