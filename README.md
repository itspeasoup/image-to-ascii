# image-to-ascii
convert an image into ascii art and then paste it anywhere! (yes i made it for ywot)

so you'll be met with a little funky window:

![obrazek](https://github.com/itspeasoup/image-to-ascii/assets/107713251/aa7fa106-15a1-4e43-8a83-8ca98f2f964a)

by the feather, you can instantly discover i used tkinter for the gui and pyinstaller for the exe.

of course, it's not rocket science, as
"open image" literally does what it says (opens explorer allowing you to **open** a thing):

![obrazek](https://github.com/itspeasoup/image-to-ascii/assets/107713251/397a8b7c-902a-4926-a2ea-1761b7b7946c)

i will be using this image.

![obrazek](https://github.com/itspeasoup/image-to-ascii/assets/107713251/6a02ada3-7ce6-4d75-a6a7-b67b72732f79)

now, your window should have the image loaded and shown:

![obrazek](https://github.com/itspeasoup/image-to-ascii/assets/107713251/0779f8e9-e72b-4010-a0b0-693b44136b14)

if you're wondering where the result is, it's directly below the "text size" value. the result is already done, i just need to scroll down because it uses ✨*spaces*✨ instead of an actual symbol for a transparent pixel. that works for white backgrounds as well!

scrolling down gives you a weird salad with some text because i'm too lazy to make a proper method of showing the result:
![obrazek](https://github.com/itspeasoup/image-to-ascii/assets/107713251/1a30d1b5-da2c-4efe-b991-d5f54fc2aab8)

to copy it, just click on the text box, then ctrl+a and then ctrl+c since there's no direct context menu for that so i hope you have a keyboard.


to see the results, **just open notepad**, and paste it in. you then get your result.

![obrazek](https://github.com/itspeasoup/image-to-ascii/assets/107713251/4f7d893f-4931-42a5-8336-0c41a24d3150)

> [!IMPORTANT]
> "I want the image bigger or smaller!" - okay billy that's what the text size is for: it works like image resolution, so making it like 10 makes it a 10x10 text canvas and it's useless for that image because it gives you one symbol:
> 
> ![obrazek](https://github.com/itspeasoup/image-to-ascii/assets/107713251/aa56406e-202c-471c-8bba-84dcb130aff3)
>
> yeah i don't think you want that
> 
> on the other hand, making the resolution size **big** like 1024 then you're gonna get an image that has MUCH higher quality but is MUCH bigger you're gonna need to zoom all the way out on that:
> ![obrazek](https://github.com/itspeasoup/image-to-ascii/assets/107713251/8441546e-9a4c-4850-acb2-ca9c6287f0e2)

> [!NOTE]
> do you see those tiny things around the black symbols?
>
> ![obrazek](https://github.com/itspeasoup/image-to-ascii/assets/107713251/6d962911-6e47-4aa4-811f-4a656f0c1482)
>
> those are **symbols too!**
> correct, the thing supports anti-aliasing too, even half-transparent images!

### okay bye i'm going to sleep
