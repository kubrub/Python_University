from PIL import Image


def convert_to_jpeg(name_of_photo):
    # Open BMP file
    bmp_image = Image.open(name_of_photo)
    
    # Convert to JPEG with standard encoding
    bmp_image.convert("RGB").save("example1.jpg", "JPEG")

    # Close BMP and JPEG files
    bmp_image.close()

'''from PIL import Image

# Open BMP file
bmp_image = Image.open("example.bmp")

# Convert to JPEG with standard encoding
jpeg_image = bmp_image.convert("RGB").save("example.jpg", "JPEG")

# Close BMP and JPEG files
bmp_image.close()
jpeg_image.close()
'''