from PIL import Image


print("RUNING___________")

# Open image
image = Image.open('./images/duck.png')

# Resize and save image

new_image = image.resize((800, 800))
new_image.save('./images/duck_resized.png')



# Print image size
print(image.size)
print(new_image.size)



#print(image)
#image.show()


# The file format of the source file.
#print(image.format) # Output: JPEG

# The pixel format used by the image. Typical values are "1", "L", "RGB", or "CMYK."
#print(image.mode) # Output: RGB

# Image size, in pixels. The size is given as a 2-tuple (width, height).
#print(image.size) # Output: (1920, 1280)

# Colour palette table, if any.
#print(image.palette) # Output: None