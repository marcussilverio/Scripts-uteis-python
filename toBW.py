from PIL import Image
path = input("path: ")
color_image = Image.open(path)
gray_scale = color_image.convert("L")
gray_scale.save("converted_"+path)