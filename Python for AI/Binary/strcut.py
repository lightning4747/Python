import struct

# Data to write
data = (42, 3.14, True, b'PY') # An int, a float, a bool, and 2 bytes

# Pack the data into a bytes object.
# Format: '<' (little-endian), 'i' (4-byte int), 'f' (4-byte float),
#         '?' (1-byte bool), '2s' (2-byte string/bytes)
packed_data = struct.pack('<if?2s', *data)
print(f"Packed Bytes: {packed_data}") # Looks like garbage: b'*\x00\x00\x00\xc3\xf5H@\x01PY'

# Write the packed bytes to a binary file
with open('data.bin', 'wb') as file: # Note 'wb' for Write Binary
    file.write(packed_data)

# Read the raw bytes back from the file
with open('data.bin', 'rb') as file: # Note 'rb' for Read Binary
    raw_bytes = file.read()

# Unpack the bytes into a tuple of Python objects
unpacked_data = struct.unpack('<if?2s', raw_bytes)
print(f"Unpacked Data: {unpacked_data}") # Output: (42, 3.140000104904175, True, b'PY')
# Note the float imprecision - inherent to floating-point representation.