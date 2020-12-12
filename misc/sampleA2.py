# object representation

from PIL import Image, ImageDraw
import webbrowser
import math
import csv
import array as arr


filename = "sampleA2.png"
img = Image.new('RGB', (600, 600))

# this list hold all vertices
# you can use append() to add all x, y, z
# into it. the format could be like this:
# [[x1, y1, z1], [x2, y2, z2],......]
vertices = []


#read in face vertices
with open('face-vertices.data') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:    

        print( float(row[0]), float(row[1]), float(row[2]) )

    
pixels = img.load()
def draw_pixel(x,y, color):
    pixels[x,y] = (color,0,0)

#read index
with open('face-index.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for index in csv_reader:
        if line_count < len(index):
            print( int(index[0]), int(index[1]), int(index[2]) )

        #Used as a tool to draw in image?    
        draw = ImageDraw.Draw(img)

        draw.line((0,0,200,200), fill=255)


#img.show()

img.save(filename)
webbrowser.open(filename)
