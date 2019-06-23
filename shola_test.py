def solutions(S, K):
    joined_list = S.split("-")
    joined_string = "".join(joined_list)
    # print(joined_string)

    reversed_list = list(joined_string)
    reversed_list.reverse()
    reversed_string = "".join(reversed_list)

    output = ''

    for index, char in enumerate(reversed_string):
        if (index) % K == 0 and index != 0:
            output += "-"
        output += char

    # print(reversed_string)
    # print(output)
    output_list = list(output)
    output_list.reverse()

    result = "".join(output_list)
    return(result.upper())
#
print(solutions('2-4A0r7-4k-34568', 4))


# def solution(S1, S2):
#     position = 0
#
#     time = 0
#     for char in S2:
#         each_time = abs(S1.index(char) - position)
#         position = S1.index(char)
#         time += each_time
#
#     return time
#
# print(solution('abcdefghijklmnopqrstuvwxyz', 'cba'))

# def solution(A):
#     levels = []
#     sum = 0
#     pointer = 0
#     count = 0
#     for index, num in enumerate(A):
#         sum += num
#         count += 1
#         if (count % 2**pointer) == 0:
#             levels.append(sum)
#             sum = 0
#             pointer += 1
#             count = 0
#
#     print(levels)
#     return levels.index(max(levels)) + 1

# import math
# def solution(A):
#     length = math.floor(math.log10(len(A))/math.log10(2))
#     length += 1
#     # print(length+1)
#     levels = [0]*int(length)
#     pointer = 0
#     count = 1
#     raised = 0
#     for index, num in enumerate(A):
#         levels[pointer] += num
#         count += 1
#         if (count % 2 ** raised) == 0:
#             pointer += 1
#             count = 0
#             raised += 1
#
#     print(levels)
#     return max(levels)
#
# print(solution([-1,7,0,7,2,3,4,1]))

# def cash_register(PP, CH):
#     result = []
#
#     change_amount = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
#     change_value = ['ONE HUNDRED', 'FIFTY', 'TWENTY', 'TEN', 'FIVE', 'TWO', 'ONE', 'HALF DOLLAR', 'QUARTER', 'DIME',
#                     'NICKEL', 'PENNY']
#     if PP > CH:
#         return "ERROR"
#     elif PP == CH:
#         return "ZERO"
#     else:
#         amount = CH - PP
#         index = 0
#         while amount > 0:
#             if amount >= change_amount[index]:
#                 amount -= change_amount[index]
#                 result.append(change_value[index])
#                 print(change_amount[index])
#             else:
#                 index += 1
#
#         return sorted(result)
#
#
# print(cash_register(1.75, 100))


