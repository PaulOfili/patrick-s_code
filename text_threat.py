sentence = 'xaxax'
sentence = sentence.lower()
score = 0


def check_palindrome(segment):
    reversed = segment[::-1]
    return reversed == segment


# for begin in range(len(sentence)-2):
#     for stop in range(3, len(sentence)+1):
#         end = begin + stop
#         if end > len(sentence):
#             continue

for begin in range(len(sentence)-2):
    for stop in range(begin + 3, len(sentence)+1):
        # end = begin + stop
        # if end > len(sentence):
        #     continue

        segment = sentence[begin:stop]

        # print(begin, begin + stop)
        print(segment)

        result = check_palindrome(segment)

        if result:
            score += len(segment)


print(score)

# stuff = '232323abc'
# print(stuff[-3:])