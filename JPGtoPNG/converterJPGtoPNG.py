import sys
import os
from PIL import Image

#sgrab first & second argument
imageFolder = sys.argv[1]
finalFolder = sys.argv[2]

#check is second argument exist and if not create it
if not os.path.exists(finalFolder):
    os.makedirs(finalFolder)

#loop through folder(first argument) and convert images to PNG
for image in os.listdir(imageFolder):
    img = Image.open(f"{imageFolder}{image}")
    clean_name = os.path.splitext(image)[0]
    img.save(f"{finalFolder}{clean_name}.png", "png")

print("Work done!")
