# a = [12, 16]
# b = list(range(1, 11))
# result = []
#
# for num in b:
#     check = True
#     for div in a:
#         if not div % num == 0:
#             check = False
#             break
#     if check:
#         result.append(num)
#
# print(result)

def binary(num):

    rem = num
    output = ""

    while rem > 0:
        output = str((rem % 2))  + output
        rem = rem // 2

    count = 0
    count_each = 0

    for num in output:
        if num == '1':
            count_each += 1
        else:
            count_each = 0
        count = max(count, count_each)

    print(count)
    return int(output)

print(binary(28))

