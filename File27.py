from struct import *

print('Введите N - количество элементов в файле')
N = int(input())

with open('27.bin', 'wb') as f:
    for i in range(1, N + 1):
        f.write(pack('>i', i))

with open('27.bin', 'rb') as f:
    s = []
    for value in iter_unpack('>i', f.read()):
        s.append(value[0])

    print(f'Изначальный порядок чисел в файле: {s}')

    k = 1
    for i in range(len(s) // 2):
        l = s.pop(-1)
        s.insert(k, l)
        k += 2

    print(f'Измененный порядок чисел в файле: {s}')