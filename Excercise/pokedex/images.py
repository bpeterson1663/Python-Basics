from PIL import Image, ImageFilter

img = Image.open('./pokemon/pikachu.jpg')

filtered_img = img.filter(ImageFilter.EMBOSS)

filtered_img.save("./pokemon/embos.png", "png")
greyed_image = img.convert("L").resize((300,300))

filtered_img.show()
greyed_image.show() 