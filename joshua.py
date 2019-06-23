def programmer_year(year):
    day = 256
    index = 0

    if year != 1918:
        if year < 1918:
            if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):
                months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            else:
                months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        elif year > 1918:
            if year % 4 == 0:
                months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            else:
                months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    else:
        months = [31, 15, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while day > months[index]:
        day = day - months[index]
        index += 1

    if year == 1918:
        if index == 1:
            result_day = 13 + day
        else:
            result_day = day
    else:
        result_day = day

    result_month = index + 1
    result_year = year

    return result_day, result_month, result_year


print(programmer_year(1800))
