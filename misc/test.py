from PIL import Image, ImageDraw
from random import randint
picture = Image.new("RGB", (600, 600))
artist = ImageDraw.Draw(picture)
for i in range(100):
    x1, y1 = randint(0, 600), randint(0, 600)
    x2, y2 = randint(0,600), randint(0,600)
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    width = randint(2, 20)
    artist.line([x1, y1, x2, y2], color, width)
#picture.convert("RGB")
#picture.show()
# save the image to show it with the web browser's viewer
filename = "aa_image.jpg"
picture.save(filename)
import webbrowser
webbrowser.open(filename)
