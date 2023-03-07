import struct


with open('CompressedImage', 'wb') as f:

    for i in range(256):

        value = format(i, '08b') # Convert number in binary

        int_value = int(value, 2)

        packed_value = struct.pack('B', int_value)
        f.write(packed_value)
