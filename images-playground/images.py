from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
blurred_image = img.filter(ImageFilter.BLUR)
blurred_image.save("blur.png", "png")
sharpened_image = img.filter(ImageFilter.SHARPEN)
sharpened_image.save("sharpen.png", "png")