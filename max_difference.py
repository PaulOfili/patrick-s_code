import math


# def max_difference(arr):
#     max_even = float('-inf')
#     min_odd = float('inf')
#
#     # arr = sorted(arr)
#
#     for num in arr:
#         if num % 2 == 0 and num < max_even:
#             max_even = num
#         elif num % 2 != 0 and num < min_odd:
#             min_odd = num
#             max_even = float('-inf')
#         # print(min_odd, max_even)
#     if max_even == -math.inf or min_odd == math.inf:
#         return -1
#     else:
#         return max_even - min_odd




def max_difference(arr):

    mini = maxi = arr[0]

    for num in arr[1:]:
        if num % 2 != 0 and num < mini:
            mini = num
            maxi = num
        elif num % 2 == 0 and num > maxi:
            maxi = num

        print(mini, maxi)

    if maxi - mini == 0 or mini % 2 == 0:
        return -1
    else:
        return maxi - mini


print(max_difference([1,2,3,6,4]))
print(max_difference([2,4,6,8,10]))
print(max_difference([5,4,3,2,1]))
print(max_difference([1,2,3,4,5]))