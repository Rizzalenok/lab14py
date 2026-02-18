from struct import *
import os

print('Введите N - количество элементов в файле')
N = int(input())

with open('36.bin', 'wb') as f:
    for i in range(1, N + 1):
        f.write(pack('>i', i))

with open('36.bin', 'rb') as f:
    data = f.read()
    s1 = []
    for value in iter_unpack('>i', data):
        s1.append(value[0])

    print(f'\nИзначальный порядок чисел в файле: {s1}')
    print(f'Изначальный размер файла: {os.path.getsize('36.bin')} байт')

with open('36.bin', 'ab') as f:
    for value in iter_unpack('>i', data):
        f.write(pack('>i', value[0]))

with open('36.bin', 'rb') as f:
    s2 = []
    data1 = f.read()
    for value in iter_unpack('>i', data1):
        s2.append(value[0])

    print(f'\nИзмененный порядок чисел в файле: {s2}')
    print(f'Измененный размер файла: {os.path.getsize('36.bin')} байт')