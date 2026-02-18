from struct import *

print('Вывод содержимого первого файла: ')
with open('1.bin', 'rb') as f:
    for value in iter_unpack('>d', f.read()):
        print(value[0])

with open('1.bin', 'rb') as f:
    data = f.read()
    s = []
    for value in iter_unpack('>d', data):
        s.append(value[0])


with open('2.bin', 'wb') as f:
    f.write(pack('>dd', s[0], s[-1]))

print('\nВывод содержимого второго файла: ')
with open('2.bin', 'rb') as f:
    for value in iter_unpack('>d', f.read()):
        print(value[0])