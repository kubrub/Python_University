import struct


def bmp(name_of_photo):
    # Open BMP file and read header
    with open(name_of_photo, "rb") as bmp_file:
        bmp_data = bmp_file.read()
        bmp_header = bmp_data[:54]

        # Get image dimensions
        width, height = struct.unpack("<LL", bmp_header[18:26])
        bpp = struct.unpack("<H", bmp_header[28:30])[0]

        # Set RLE compression flag
        bmp_header = bmp_header[:30] + struct.pack("<I", 3) + bmp_header[34:]

        # Create RLE compressed image data
        rle_data = bytearray()
        row_length = ((width * bpp + 31) // 32) * 4  # Round up to nearest 32-bit boundary
        for y in range(height):
            row_start = 54 + y * row_length
            row_end = row_start + row_length
            row_data = bmp_data[row_start:row_end]
            rle_row_data = bytearray()
            for i in range(0, len(row_data), 2):
                count = 1
                while i + 2 < len(row_data) and row_data[i:i+2] == row_data[i+2:i+4]:
                    count += 1
                    i += 2
                if count > 1:
                    rle_row_data += struct.pack("<BB", count + 128, row_data[i])
                else:
                    rle_row_data += row_data[i:i+2]
            rle_data += struct.pack("<B", 0) + rle_row_data + struct.pack("<B", 0)

        # Write RLE compressed BMP file
        with open("example_rle.bmp", "wb") as rle_file:
            rle_file.write(bmp_header + bytes(rle_data))
