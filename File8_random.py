import struct
import random

N = int(input())

# numbers = [random.uniform(-100, 100) for x in range(N)]
# print(numbers)
#
# with open('1.bin', 'wb') as f:
#     for num in numbers:
#         f.write(struct.pack('>d', num))

with open('1.bin', 'rb') as f:
    for _ in range(N):
        print(struct.unpack('>d', f.read(8)))
