def allocateSchools(schoolSeatsArray, studentScoreArray, studentSchoolPreferencesArray):
    index_score = []

    for index, value in enumerate(studentScoreArray):
        index_score.append([index, value])

    sorted_index_score = sorted(index_score, key=lambda num: num[1], reverse=True)

    done = ['0'] * len(studentScoreArray)

    for index, score in sorted_index_score:
        for choice in studentSchoolPreferencesArray[index]:
            if schoolSeatsArray[choice] > 0:
                schoolSeatsArray[choice] -= 1
                done[index] = '1'
                break

    first = done.count('0')
    second = sum(schoolSeatsArray)
    output = [second, first]
    return output

