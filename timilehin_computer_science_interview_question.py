def check(string, k):
    start = 0
    last = k-1
    max_length = k
    output = ''

    if k > len(string):
        return string

    while last < len(string):
        print(start, last, output, max_length)
        segment = string[start:last+1]
        if len(set(segment)) <= k:
            if len(segment) >= max_length:
                output = segment
                max_length = len(segment)
            last += 1
        else:
            start += 1

        # last += 1
    return output


print(check('ABCDDDEEEFF', 11))
