"""TRY TO LOOP FROM THE START AND ONLY THE ONES REQUIREDDDDD"""


def new_year(arr):
    start = list(range(1, len(arr) + 1))
    start.reverse()
    print(start)
    start_enum = enumerate(start)
    start_dict = {val: index for index, val in start_enum}
    print(start_dict)

    new_arr = arr[:]
    new_arr.reverse()
    new_arr_enum = enumerate(new_arr)
    new_arr_dict = {val: index for index, val in new_arr_enum}
    print(new_arr_dict)

    count = 0
    check_chaos = False
    for num in arr:
        count_each = 0
        if check_chaos:
            break
        while start_dict[num] != new_arr_dict[num]:


                # break

            # print(num, count_each)

            print(num, start_dict, count_each)

            num_pos = start_dict[num]
            next_ele = start[num_pos + 1]

            start[start_dict[num]], start[start_dict[num] + 1] = start[start_dict[num] + 1], start[start_dict[num]]

            start_dict[num] = start_dict[num] + 1
            start_dict[next_ele] = start_dict[next_ele] - 1

            count_each += 1

            if count_each > 2:
                check_chaos = True
                    
            print(start)
            # print(num, start_dict, count_each)

        count += count_each

    # print(start_dict)

    if check_chaos:
        return "Too chaotic"
    return count


# print(new_year([2,1,5,3,4]))
print(new_year([2,5,1,3,4]))
# print(new_year(list(map(int, "1 2 5 3 7 8 6 4".split(" ")))))
# print(new_year(list(map(int, "5 1 2 3 7 8 6 4".split(" ")))))
