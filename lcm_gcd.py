def gsd(x, y):
    while(y):
        x, y = y, x % y
        # print(x, y)

    return x

print(gsd(6,9))
