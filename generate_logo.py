# converts a given image file into a ico file
from PIL import Image
filename = r'compass_icon.png'
img = Image.open(filename)
img.save('logo.ico')