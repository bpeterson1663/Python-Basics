from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.EMBOSS)
greyed_img = img.convert("L")
filtered_img.rotate(90)

greyed_img.save("greyed.png", "png")
filtered_img.save("blur.png", "png")
print(img)
print(img.format)
print(img.size)
print(img.mode)
filtered_img.show()

filtered_img.thumbnail((400, 400))
filtered_img.save('thumbnail.jpg')
