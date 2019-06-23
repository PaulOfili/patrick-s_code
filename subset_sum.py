# First Condition
def check_divisors(num):
    divisors_arr = []
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
            divisors_arr.append(i)

    return sum_of_divisors > num, divisors_arr

# Driver for Second Condition
def rec(arr, total, i, mem):
    key = str(total) + "-" + str(i)
    if key in mem:
        return mem[key]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        to_return = rec(arr, total, i - 1, mem)
    else:
        to_return = rec(arr, total, i - 1, mem) + rec(arr, total - arr[i], i - 1, mem)

    mem[key] = to_return
    return to_return

# Second Condition
def check_subset_sum(arr, total):
    mem = {}
    return rec(arr, total, len(arr) - 1, mem) == 0


# Main Function
employee_numbers = []
for employee_no in range(1, 1001):
    if check_divisors(employee_no)[0] and check_subset_sum(check_divisors(employee_no)[1], employee_no):
        employee_numbers.append(employee_no)

print(employee_numbers)

