from itertools import combinations

# 1ST SOLUTION
# def subsets(s):
#     sets = []
#     for i in range(1 << len(s)):
#         subset = [s[bit] for bit in range(len(s)) if is_bit_set(i, bit)]
#         sets.append(subset)
#     return sets
#
# def is_bit_set(num, bit):
#     return num & (1 << bit) > 0

# 2ND SOLUTION
# def subsets(s):
#     """
#     :type s: list[]
#     """
#     sets = []
#     for i in range(2**len(s)):
#         subset = []
#         for j in range(len(s)):
#             if i & (1 << j) > 0:
#                 subset.append(s[j])
#         sets.append(subset)
#     return sets

# 3RD SOLUTION
def subsets(s):
    for cardinality in range(len(s) + 1):
        yield from combinations(s, cardinality)

s = [1,2,3,4]
sub_sets = [[sub_set] for sub_set in subsets(s)]
print(sub_sets[1:])
print(len(sub_sets[1:]))