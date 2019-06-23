def scores(arr):
    def factorial(x):
        if x < 2:
            return 1
        return x * factorial(x - 1)

    score_list = sorted(arr)

    def combination(x):
        return factorial(x)//((factorial(x-2))*factorial(2))

    score_obj = {}
    for score in score_list:
        score_obj[score] = score_obj[score] + 1 if score in score_obj.keys() else 1

    output = score_obj[score_list[-2]] if score_obj[score_list[-1]] == 1 else combination(score_obj[score_list[-1]])

    possibles = combination(len(arr))
    result = round(output / possibles, 2)
    print(output, possibles)
    return result

print(scores([1, 2, 2, 3, 7, 7]))