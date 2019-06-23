# arr = [1,2,3,4,5]
# #
# # index = [k for k in (enumerate(arr))]
# #
# # print(index)
#
# # arr2 = [5,6,7,8,9]
# #
# # arr1 = arr2
# #
# # print(arr1)
#
# arr1 = []
#
# arr1[0] = 4
#
# print(arr1)
# remaining_tasks = [5,4,7]

# prev = remaining_tasks[0]
# remaining_tasks[0] = None


#
# for index, task in enumerate(remaining_tasks[1:]):
#     # if abs(task - prev) >= 2:
#     #     prev = task
#     #     remaining_tasks[index] = None
#     #
#     # print(prev)
#     # print(remaining_tasks)
#     print(index, task)

# count = 2

# def stuff():
#     if count == 2:
#         return count
#
# stuff()

# for name, i in enumerate([5,6,7,8]):
#     print(name, i)

# from itertools import *

# x = combinations(range(4), 3)
# y = permutations()
# print(len(list(x)))

# a, b = [1, 3]
# # print(a, b)
# vis = [[]*10 for _ in range(3)]
# xi = [[1]*5 for _ in range(3)]
# xii = []*4
# print(vis)
# print(xi)
# print(xii)

# a = dict([(0,'A'),(1,'B')])
# # print(a)
# text = list('abcdefghijklmnopqrstuvwxyz/ ')
# text.reverse()
# text = "".join(text)
# print(list(iter(enumerate(text))))
# textdict = dict(list(enumerate(text)))
# textdict1 = {value: key for key, value in textdict.items()}
# print(textdict1)
#
# encoded = ''.join([str(value) for key, value in textdict1.items()])
# print(encoded)



def atm_withdraw(amount):
    remaining = amount
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5]
    output = []

    index = 0

    while remaining >= 5:
        if remaining >= denominations[index]:
            remaining -= denominations[index]
            output.append(denominations[index])
        else:
            index += 1

    print(remaining)
    return output

print(atm_withdraw(3752))
# from collections import defaultdict

# ar = defaultdict(int)
# ar['a'] = 1
# ar['b'] = 2
# if 'a' in ar.keys():
#     print('Yeah')


