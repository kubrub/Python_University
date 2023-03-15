from PIL import Image


def convert_to_tiff(name_of_photo):
    # Open BMP file
    bmp_image = Image.open(name_of_photo)

    # Convert to TIFF with LZW compression
    bmp_image.convert("RGB").save("example_lzw.tiff", compression="tiff_lzw")

    # Close BMP and TIFF files
    bmp_image.close()


'''from PIL import Image

# Open BMP file
bmp_image = Image.open("example.bmp")

# Convert to TIFF with LZW compression
tiff_image = bmp_image.convert("RGB").save("example_lzw.tiff", compression="tiff_lzw")

# Close BMP and TIFF files
bmp_image.close()
tiff_image.close()
'''
