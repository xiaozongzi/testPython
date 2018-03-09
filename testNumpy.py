from functools import reduce

import numpy as np

sums = 0
for each in range(1, 51):
    first = (each * 2 - 1)
    second = (each * 2)
    print([first, second])
    sums += first * second
    print(sums)
sums = 0


# for each in range(1, 100, 2):
#     sums += each * (each + 1)
#     print(sums)


def add(x, y):
    print(x, y)
    if x == 1:
        x = 2
    return x + (y * (y + 1))


res = reduce(add, range(1, 100, 2))
print(res)


def add2(x, y):
    print(x, y)
    return x + (y * (y - 1))


res = reduce(add2, range(0, 101, 2))
print(res)

print(np.exp([0, 1, 2,0.5,-0.5]))
