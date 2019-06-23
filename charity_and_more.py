# def charity(arr) :
#     sums = [arr[0], arr[1], arr[2]]
#     grp = ['A', 'B', 'C']
#     output = ['A', 'B', 'C']
#
#     for money_index in range(len(arr)):
#         if money_index < 3:
#             continue
#         minimum = min(sums)
#         output.append(grp[sums.index(minimum)])
#         sums[sums.index(minimum)] += arr[money_index]
#
#     return output
#
#
# print(charity([25,8,2,35,15,120,55,42]))


# def stock(arr):
#     cost = []
#
#     for row in arr:
#         calc_cost = (row[2] - row[1])/row[1]
#         cost.append(calc_cost)
#
#     return arr[cost.index(min(cost))][0]
#
#
# print(stock([[1200, 100, 105], [1400, 50, 55]]))


# def charity(arr):
#     charities = {'A': 0, 'B': 0, 'C': 0}
#     output = []
#
#     for money in arr:
#         lowest = min(charities.values())
#         org = list(charities.keys())[list(charities.values()).index(lowest)]
#         output.append(org)
#         charities[org] += money
#
#     return output
#
#
# print(charity([25,8,2,35,15,120,55,42]))


# def min_slice(arr):
#     cost_of_slice = []
#
#     for row in arr:
#         if arr.index(row) == 0:
#             cost_of_slice = row[:]
#             prev_indexes = [index for index, val in enumerate(row)]
#             print(prev_indexes)
#             continue
#         for col_index in range(len(arr)):
#             if prev_indexes[col_index] == 0:
#                 minimum = min(row[prev_indexes[col_index]],
#                               row[prev_indexes[col_index] + 1])
#
#             elif prev_indexes[col_index] == len(arr) - 1:
#                 minimum = min(row[prev_indexes[col_index]],
#                               row[prev_indexes[col_index] - 1])
#
#             else:
#                 minimum = min(row[prev_indexes[col_index]],
#                               row[prev_indexes[col_index] + 1],
#                               row[prev_indexes[col_index] - 1])
#
#             for num in row:
#                 if num == minimum and abs(prev_indexes[col_index] - row.index(num)) < 2:
#                     prev_indexes[col_index] = row.index(num)
#                     break
#
#             cost_of_slice[col_index] += minimum
#         print(prev_indexes)
#         # print(cost_of_slice)
#
#     print(cost_of_slice)
#     return min(cost_of_slice)
#
#
# # print(min_slice([[1,3,2,5],
# #                  [3,2,2,1],
# #                  [5,3,8,1],
# #                  [5,12,14,1]]))
# print(min_slice([[1,2,3],
#                  [4,5,6],
#                  [7,8,9]]))

# def min_slice(arr):
#     cost_of_slice = []
#
#     for row_index in range(len(arr)):
#         if arr.index(row_index) == 0:
#             cost_of_slice = row_index[:]
#             continue
#         for col_index in range(len(arr)):
#             if col_index == 0:
#                 minimum = min(arr[row_index - 1][col_index],
#                               arr[row_index - 1][col_index + 1])
#
#             elif col_index == len(arr) - 1:
#                 minimum = min(arr[row_index - 1][col_index],
#                               arr[row_index - 1][col_index - 1])
#
#             else:
#                 minimum = min(arr[row_index - 1][col_index - 1],
#                               arr[row_index - 1][col_index],
#                               arr[row_index - 1][col_index + 1])
#
#             cost_of_slice[col_index] += arr[row_index][col_index] + minimum
#         # print(prev_indexes)
#         # print(cost_of_slice)
#
#     print(cost_of_slice)
#     return min(cost_of_slice)
#
#
# # print(min_slice([[1,3,2,5],
# #                  [3,2,2,1],
# #                  [5,3,8,1],
# #                  [5,12,14,1]]))
# print(min_slice([[1,2,3],
#                  [4,5,6],
#                  [7,8,9]]))

# def min_slice(arr):
#     cost_of_slice = []
#
#     for row_index in range(len(arr)):
#         if row_index == 0:
#             cost_of_slice = arr[row_index][:]
#             continue
#         # temp_cost_of_slice = [0]*len(arr)
#         temp_cost_of_slice = []
#
#         for col_index in range(len(arr)):
#             if col_index == 0:
#                 minimum = min(cost_of_slice[col_index],
#                               cost_of_slice[col_index + 1])
#
#             elif col_index == len(arr) - 1:
#                 minimum = min(cost_of_slice[col_index],
#                               cost_of_slice[col_index - 1])
#
#             else:
#                 minimum = min(cost_of_slice[col_index - 1],
#                               cost_of_slice[col_index],
#                               cost_of_slice[col_index + 1])
#
#             # temp_cost_of_slice[col_index] = arr[row_index][col_index] + minimum
#             temp_cost_of_slice.append(arr[row_index][col_index] + minimum)
#
#         cost_of_slice = temp_cost_of_slice
#
#     print(cost_of_slice)
#     return min(cost_of_slice)
#
#
# print(min_slice([[10,3,2,5,1],
#                  [1,1,2,1,1],
#                  [5,1,8,9,1],
#                  [5,10,1,4,1],
#                  [4,2,4,1,4]]))
# print(min_slice([[1,2,3],
#                  [4,5,6],
#                  [7,8,9]]))

arr = [1,2,3,4]
res = []
for i in range(3):
    for j in range(i+1, 4):
        res.append(arr[i] + arr[j])
print(res)