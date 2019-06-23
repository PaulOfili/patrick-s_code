# How to squeeze an array
input_arr = [[1, 2, 3, 4, 17],
             [5, 6, 7, 8, 18],
             [9,10,11,12, 19],
             [13,14,15,16, 20]]
m = 4
n = 5

# range_index = [(0,0), (1,1)]

# input_arr = [[9718805, 60013003, 5103628, 85388216, 21884498, 38021292, 73470430, 31785927],
#             [69999937 ,71783860 ,10329789 ,96382322 ,71055337 ,30247265 ,96087879 ,93754371],
#             [79943507 ,75398396 ,38446081 ,34699742 ,1408833 ,51189 ,17741775, 53195748],
#             [79354991 ,26629304 ,86523163 ,67042516 ,54688734 ,54630910 ,6967117 ,90198864],
#             [84146680 ,27762534 ,6331115 ,5932542 ,29446517 ,15654690 ,92837327 ,91644840],
#             [58623600 ,69622764 ,2218936 ,58592832 ,49558405 ,17112485 ,38615864 ,32720798],
#             [49469904 ,5270000 ,32589026 ,56425665 ,23544383 ,90502426 ,63729346 ,35319547],
#             [20888810 ,97945481 ,85669747 ,88915819 ,96642353 ,42430633 ,47265349 ,89653362],
#             [55349226 ,10844931 ,25289229 ,90786953 ,22590518 ,54702481 ,71197978 ,50410021],
#             [9392211, 31297360, 27353496, 56239301, 7071172, 61983443, 86544343, 43779176]]

for x in range(min(m, n)//2):
    squeezed_arr = [[], [], [], []]
    r = 14
    for i in range(x, m-x):
        for j in range(x, n-x):
            if i == x:
                squeezed_arr[0].append(input_arr[i][j])
            elif j == n - 1 - x:
                squeezed_arr[1].append(input_arr[i][j])
            elif i == m - 1 - x:
                squeezed_arr[2].append(input_arr[i][j])
            elif j == x:
                squeezed_arr[3].append(input_arr[i][j])

    print(squeezed_arr)

    squeezed_list = squeezed_arr[0]
    for index in range(1, len(squeezed_arr)):
        if index >= len(squeezed_arr)//2:
            squeezed_arr[index].reverse()
            squeezed_list.extend(squeezed_arr[index])
        else:
            squeezed_list.extend(squeezed_arr[index])

    print(squeezed_list)

    r = r % len(squeezed_list)
    new_squeezed_list = []
    for index in range(len(squeezed_list)):
        new_index = index + r
        if new_index > len(squeezed_list) - 1:
            new_index %= len(squeezed_list)

        new_squeezed_list.append(squeezed_list[new_index])

    print(new_squeezed_list)

    for i in range(x, m-x):
        for j in range(x, n-x):
            if i == x:
                input_arr[i][j] = new_squeezed_list[i + j - (2*x)]
            elif j == n - 1 - x:
                # print(i , j)
                input_arr[i][j] = new_squeezed_list[i + j - (2*x)]
            elif i == m - 1 - x:
                input_arr[i][j] = new_squeezed_list[len(squeezed_list)-(i+j) + (2*x)]
            elif j == x:
                input_arr[i][j] = new_squeezed_list[len(squeezed_list)-(i+j) + (2*x)]

for row in input_arr:
    for col in row:
        print(col,end=" ")
    print(end="\n")