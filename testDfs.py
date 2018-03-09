def f(s, a, b):
    if a == 0 and b == 0:
        print(s)
        return
    if b > 0:
        f(s + ")", a, b - 1)
    if a > 0:
        f(s + "(", a - 1, b + 1)


f("", 3, 0)
