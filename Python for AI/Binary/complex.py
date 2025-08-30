import struct

# Read the first 54 bytes of a BMP file (the header)
with open('image.bmp', 'rb') as file:
    # Read the full header
    header = file.read(54)

    # Unpack specific fields from the header
    # Format: '<2sI' -> little-endian, 2-byte string (signature 'BM'), 4-byte int (file size)
    signature, file_size = struct.unpack('<2sI', header[:6])
    width, height = struct.unpack('<2I', header[18:26]) # 2 unsigned ints at offsets 18 and 22
    # The offsets (18, 26) are defined by the BMP file format specification.

print(f"Signature: {signature}") # Should be b'BM'
print(f"File Size: {file_size} bytes")
print(f"Image Dimensions: {width}x{height}")