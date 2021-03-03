from PIL import Image, ImageFilter

image = Image.open('sample_pillow.jpg')

print(image.format, image.size, image.mode)

resize_img = image.resize( (531 , 394), Image.LANCZOS) 

resize_img.save("sample_pillowsss.JPG")
image_pillow = Image.open('sample_pillowsss.jpg')

print(image_pillow.format, image_pillow.size, image_pillow.mode)
