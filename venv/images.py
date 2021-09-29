from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.EMBOSS)
greyed_img = img.convert("L")
greyed_img.save("greyed.png", "png")
filtered_img.save("blur.png", "png")
print(img)
print(img.format)
print(img.size)
print(img.mode)

