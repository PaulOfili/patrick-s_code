def wrap(string, num):
    result = []
    seg = ""
    count = 0
    for char in string:
        seg += char
        count += 1

        if count > num-1:
            result.append(seg)
            count = 0
            seg = ""

    temp = len(string) // num
    last = string[(temp*num):]
    result.append(last)

    return result

print(wrap("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5))