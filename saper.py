import os
import random


x = int(input('X='))          # settings
y = int(input('Y='))          # settings
bombs = int(input('Mines='))  # settings
while bombs >= x * y:             # Закоментировать при статичных настройках
    print('Too many mines')       # Закоментировать при статичных настройках
    bombs = int(input('Mines='))  # Закоментировать при статичных настройках
os.system('cls')                  # Закоментировать при статичных настройках
b = [[0 for c in range(x)] for m in range(y)]
mask = [[False for c1 in range(x)] for m1 in range(y)]
for i in range(bombs):
    a = random.randint(0, x * y - 1)
    while b[a//x][a % x] != 0:
        a = random.randint(0, x * y - 1)
    b[a//x][a % x] = -1
for x1 in range(x):
    for y1 in range(y):
        if b[y1][x1] == 0:
            for x2 in range(-1, 2):
                for y2 in range(-1, 2):
                    if -1 < x1 + x2 < x and -1 < y1 + y2 < y and b[y1 + y2][x1 + x2] == -1:
                        b[y1][x1] = b[y1][x1] + 1
igrovoepole = (u'\u250F\u2501\u2501\u2501\u2533' + '\u2501\u2501\u2501\u2533' * (x - 2) + '\u2501\u2501\u2501\u2513\n' +
              (u'\u2503\u0020\u0020\u0020\u2503' + '\u0020\u0020\u0020\u2503' * (x - 2) + '\u0020\u0020\u0020\u2503\n'
               u'\u2523\u2501\u2501\u2501\u254B' + '\u2501\u2501\u2501\u254B' * (x - 2) + '\u2501\u2501\u2501\u252B\n') * (y-1) +
               u'\u2503\u0020\u0020\u0020\u2503' + '\u0020\u0020\u0020\u2503' * (x - 2) + '\u0020\u0020\u0020\u2503\n'
               u'\u2517\u2501\u2501\u2501\u253B' + '\u2501\u2501\u2501\u253B' * (x - 2) + '\u2501\u2501\u2501\u251B')
while True:
    os.system('cls')
    for x1 in range(x):
        for y1 in range(y):
            if mask[y1][x1]:
                if b[y1][x1] == -1:
                    igrovoepole = igrovoepole[:(10 + 4 * (x - 2)) * (y1 * 2 + 1) + 2 + x1 * 4] + '\u20DD' + igrovoepole[(10 + 4 * (x - 2)) * (y1 * 2 + 1) + 3 + x1 * 4:]
                else:
                    igrovoepole = igrovoepole[:(10 + 4 * (x - 2)) * (y1 * 2 + 1) + 2 + x1 * 4] + str(b[y1][x1]) + igrovoepole[(10 + 4 * (x - 2)) * (y1 * 2 + 1) + 3 + x1 * 4:]
    print(igrovoepole, b)
    inpx = int(input('No bomb on: X='))
    inpy = int(input('Y='))
    while not -1 < inpx < x or not -1 < inpy < y or mask[inpy][inpx]:
        print('Error')
        inpx = int(input('No bomb on: X='))
        inpy = int(input('Y='))
    if b[inpy][inpx] == -1:
        os.system('cls')
        print('Lose')
        for x1 in range(x):
            for y1 in range(y):
                if b[y1][x1] == -1:
                    igrovoepole = igrovoepole[:(10 + 4 * (x - 2)) * (y1 * 2 + 1) + 2 + x1 * 4] + '\u20DD' + igrovoepole[(10 + 4 * (x - 2)) * (y1 * 2 + 1) + 3 + x1 * 4:]
                else:
                    igrovoepole = igrovoepole[:(10 + 4 * (x - 2)) * (y1 * 2 + 1) + 2 + x1 * 4] + str(b[y1][x1]) + igrovoepole[(10 + 4 * (x - 2)) * (y1 * 2 + 1) + 3 + x1 * 4:]
        print(igrovoepole)
        break
    mask[inpy][inpx] = True
    q = True
    if b[inpy][inpx] == 0:
        while q:
            q = False
            for x1 in range(x):
                for y1 in range(y):
                    if b[y1][x1] == 0:
                        for x2 in range(-1, 2):
                            for y2 in range(-1, 2):
                                if -1 < x1 + x2 < x and -1 < y1 + y2 < y:
                                    if not mask[y1 + y2][x1 + x2]:
                                        mask[y1 + y2][x1 + x2] = True
                                        q = True
    o = 0
    for x1 in range(x):
        for y1 in range(y):
            if mask[y1][x1]:
                o += 1
    if o == x * y - bombs:
        os.system('cls')
        print('win')
        for x1 in range(x):
            for y1 in range(y):
                if b[y1][x1] == -1:
                    igrovoepole = igrovoepole[:(10 + 4 * (x - 2)) * (y1 * 2 + 1) + 2 + x1 * 4] + '\u20DD' + igrovoepole[(10 + 4 * (x - 2)) * (y1 * 2 + 1) + 3 + x1 * 4:]
                else:
                    igrovoepole = igrovoepole[:(10 + 4 * (x - 2)) * (y1 * 2 + 1) + 2 + x1 * 4] + str(b[y1][x1]) + igrovoepole[(10 + 4 * (x - 2)) * (y1 * 2 + 1) + 3 + x1 * 4:]
        print(igrovoepole)
        break
input()
