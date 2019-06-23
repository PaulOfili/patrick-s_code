# FIRST APPROACH
import string

a = 'JACK'
b = 'DANIEL'


def morganAndString(a, b):
    a_list = list(a)
    b_list = list(b)

    result = []
    # letters_order = string.ascii_uppercase
    # while a_list and b_list:
    #     if letters_order.index(a_list[0]) >= letters_order.index(b_list[0]):
    #         result.append(b_list.pop(0))
    #     else:
    #         result.append(a_list.pop(0))

    while a_list and b_list:
        if ord(a_list[0]) >= ord(b_list[0]):
            result.append(b_list.pop(0))
        else:
            result.append(a_list.pop(0))

    result.extend(a_list if a_list else b_list)

    print("".join(result))


morganAndString(a, b)
