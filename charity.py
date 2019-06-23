from collections import defaultdict
input_arr \
    = [
        ['09-01', 'Arlene', '540', '570'],
        ['09-01', 'Bobby', '540', '543'],
        ['09-01', 'Caroline', '540', '530'],
        ['09-02', 'Arlene', '540', '580'],
        ['09-02', 'Bobby', '540', '580'],
        ['09-02', 'Caroline', '540', '595']
    ]
one = defaultdict(list)
new_arr = [[] for i in range(len(input_arr))]
print(new_arr)
for i in input_arr:
    for j in i[0]:
        one




