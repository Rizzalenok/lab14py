from struct import *
from random import *

N = int(input('Введите количество файлов (от 1 до 4): '))
if 1 <= N <= 4:
    pass
else:
    print('\nВведите число от 1 до 4!')
    N = int(input('Введите количество файлов: '))

with open('S0.bin', 'wb') as f1:
    for i in range(1, N + 1):
        with open(f'S{i}.bin', 'rb') as f2:
            k = 0
            for value in iter_unpack('>i', f2.read()):
                k += 1
            f1.write(pack('>i', k))
            f1.write(pack('>i', 1111111111))
            f2.seek(0)
            for value in iter_unpack('>i', f2.read()):
                f1.write(pack('>i', value[0]))
            f1.write(pack('>i', 1111111111)) # чтобы разделять блоки

with open(f'S0.bin', 'rb') as f:
         for value in iter_unpack('>i', f.read()):
             print(value[0])

# Для просмотра данных внутри файлов:
for i in range(1, N + 1):
    print(f'Числа внутри файла номер {i}')
    with open(f'S{i}.bin', 'rb') as f:
        for value in iter_unpack('>i', f.read()):
            print(value[0])