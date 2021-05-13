from PIL import Image
import os 

for file in os.listdir('original')
    if file.endsWith('.jpeg')
        img = Image.open(os.path.join('original',file))   # read image file
        img = img.convert('L')   # convert image to black and white
        img.save(os.path.join('new',file[:-4] + '_grey.jpeg'))   # save as a new image file