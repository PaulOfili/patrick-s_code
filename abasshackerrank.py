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


first_stage = defaultdict(list)
for data in input_arr:
    first_stage[data[0]].append(data)

print(first_stage)

second_stage = [[] for _ in range(len(first_stage))]
count = 0
for key, value in first_stage.items():
    for data in value:
        if int(data[3]) > int(data[2]):
            second_stage[count].append([data[1], int(data[3]) - int(data[2])])
        else:
            second_stage[count].append([data[1], 0])
    count += 1

print(second_stage)

third_stage = [[] for _ in range(len(second_stage))]
count = 0
for day in second_stage:
    for name, late in day:
        if late > sum([e[1] for e in day], 0)//len([e[1] for e in day]):
            third_stage[count].append([name, late - sum([e[1] for e in day], 0)//len([e[1] for e in day])])
        else:
            third_stage[count].append([name, 0])

    count += 1
print(third_stage)

result = defaultdict(int)
for data in third_stage:
    for name, late in data:
        result[name] += late

print(result)

maxi = float('-inf')
output = ""

for name, score in result.items():
    if score > maxi:
        output = name
        maxi = score

print(output)




