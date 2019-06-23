def reverseShuffleMerge(s):
    s_dict = defaultdict(int)

    for char in s:
        s_dict[char] += 1

    for key in s_dict:
        s_dict[key] //= 2

    # print(s_dict)

    last_range = int(len(s) / 2) - 1

    unique = set()

    for i in range(len(s) - last_range):
        copy_s_dict = {k: v for k, v in s_dict.items()}
        segment = ''
        for j in range(i, len(s)):
            if copy_s_dict[s[j]] > 0:
                copy_s_dict[s[j]] -= 1
                segment += s[j]
        unique.add(segment[::-1])

    print(sorted(list(unique)))
    return sorted(list(unique))[0]