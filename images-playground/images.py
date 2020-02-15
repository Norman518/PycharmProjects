from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save("blur.png", "png")
filtered_image2 = img.filter(ImageFilter.SHARPEN)
filtered_image2.save("sharpen.png", "png")