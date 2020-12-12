from PIL import Image
import webbrowser
img= Image.new('RGB', (320,240))
pixels= img.load()
for i in range(0,100):
    for j in range(0,100):
        pixels[i,j] = (254,0,0)
filename = "blank.png"
img.save(filename)
webbrowser.open(filename)