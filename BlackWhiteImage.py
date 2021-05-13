from PIL import Image

img = Image.open("img.jpeg")   # read image file
img = img.convert("L")   # convert image to black and white
img.save("newImg.jpeg")   # save as a new image file