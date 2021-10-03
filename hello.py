from PIL import Image, ImageEnhance
# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.open("rick-morty.png")

# Enhance constrast
enhancer = ImageEnhance.Contrast(img)
for i in range(1, 8):
    factor = i / 4.0
    new_img = enhancer.enhance(factor)
    new_img.show()