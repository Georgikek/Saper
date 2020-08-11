import os
import random


x = 15      # settings
y = 15      # settings
bombs = 10  # settings
b = [[0 for c in range(x)] for m in range(y)]
mask = [[False for c1 in range(x)] for m1 in range(y)]
for i in range(bombs):
    a = random.randint(0, x * y - 1)
    while b[a//x][a % x] != 0:
        a = random.randint(0, x * y - 1)
    b[a // x][a % x] = -1
for x1 in range(x):
    for y1 in range(y):
        if b[x1][y1] == 0:
            for x2 in range(-1, 2):
                for y2 in range(-1, 2):
                    if -1 < x1 + x2 < x and -1 < y1 + y2 < y and b[x1 + x2][y1 + y2] == -1:
                        b[x1][y1] = b[x1][y1] + 1
igrovoepole = (u'\u250F\u2501\u2501\u2501\u2533' + '\u2501\u2501\u2501\u2533' * (x - 2) + '\u2501\u2501\u2501\u2513\n' +
              (u'\u2503\u0020\u0020\u0020\u2503' + '\u0020\u0020\u0020\u2503' * (x - 2) + '\u0020\u0020\u0020\u2503\n'
               u'\u2523\u2501\u2501\u2501\u254B' + '\u2501\u2501\u2501\u254B' * (x - 2) + '\u2501\u2501\u2501\u252B\n') * (y-1) +
               u'\u2503\u0020\u0020\u0020\u2503' + '\u0020\u0020\u0020\u2503' * (x - 2) + '\u0020\u0020\u0020\u2503\n'
               u'\u2517\u2501\u2501\u2501\u253B' + '\u2501\u2501\u2501\u253B' * (x - 2) + '\u2501\u2501\u2501\u251B')
while True:
    os.system('cls')
    for x1 in range(x):
        for y1 in range(y):
            if mask[x1][y1]:
                if b[x1][y1] == -1:
                    igrovoepole = igrovoepole[:(10 + 4 * (x - 2)) * (x1 * 2 + 1) + 2 + y1 * 4] + '\u20DD' + igrovoepole[(10 + 4 * (x - 2)) * (x1 * 2 + 1) + 3 + y1 * 4:]
                else:
                    igrovoepole = igrovoepole[:(10 + 4 * (x - 2)) * (x1 * 2 + 1) + 2 + y1 * 4] + str(b[x1][y1]) + igrovoepole[(10 + 4 * (x - 2)) * (x1 * 2 + 1) + 3 + y1 * 4:]
    print(igrovoepole, b)
    inpy = int(input('No bomb on: X='))
    inpx = int(input('Y='))
    while not -1 < inpx < x or not -1 < inpy < y or mask[inpx][inpy]:
        print('Error')
        inpy = int(input('No bomb on: X='))
        inpx = int(input('Y='))
    if b[inpx][inpy] == -1:
        os.system('cls')
        print('Lose')
        mask = [[True for c in range(x)] for m in range(y)]
        for x1 in range(x):
            for y1 in range(y):
                if mask[x1][y1]:
                    if b[x1][y1] == -1:
                        igrovoepole = igrovoepole[:(10 + 4 * (x - 2)) * (x1 * 2 + 1) + 2 + y1 * 4] + '\u20DD' + igrovoepole[(10 + 4 * (x - 2)) * (x1 * 2 + 1) + 3 + y1 * 4:]
                    else:
                        igrovoepole = igrovoepole[:(10 + 4 * (x - 2)) * (x1 * 2 + 1) + 2 + y1 * 4] + str(b[x1][y1]) + igrovoepole[(10 + 4 * (x - 2)) * (x1 * 2 + 1) + 3 + y1 * 4:]
        print(igrovoepole)
        break
    mask[inpx][inpy] = True
    q = True
    while q:
        q = False
        if b[inpx][inpy] == 0:
            for x1 in range(x):
                for y1 in range(y):
                    if b[x1][y1] == 0:
                        for x2 in range(-1, 2):
                            for y2 in range(-1, 2):
                                if -1 < x1 + x2 < x and -1 < y1 + y2 < y and not mask[x1 + x2][y1 + y2]:
                                    mask[x1 + x2][y1 + y2] = True
                                    q = True
    o = 0
    for x1 in range(x):
        for y1 in range(y):
            if mask[x1][y1]:
                o += 1
    if o == x * y - bombs:
        os.system('cls')
        print('win')
        mask = [[True for c in range(x)] for m in range(y)]
        for x1 in range(x):
            for y1 in range(y):
                if mask[x1][y1]:
                    if b[x1][y1] == -1:
                        igrovoepole = igrovoepole[:(10 + 4 * (x - 2)) * (x1 * 2 + 1) + 2 + y1 * 4] + '\u20DD' + igrovoepole[(10 + 4 * (x - 2)) * (x1 * 2 + 1) + 3 + y1 * 4:]
                    else:
                        igrovoepole = igrovoepole[:(10 + 4 * (x - 2)) * (x1 * 2 + 1) + 2 + y1 * 4] + str(b[x1][y1]) + igrovoepole[(10 + 4 * (x - 2)) * (x1 * 2 + 1) + 3 + y1 * 4:]
        print(igrovoepole)
        break
input()
