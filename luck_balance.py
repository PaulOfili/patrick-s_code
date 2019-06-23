def luckBalance(k, contests):
    score = 0
    # importants = []
    #
    # for contest in contests:
    #     if contest[1] == 1:
    #         importants.append(contest)
    #
    # for i in range(len(importants)):
    #     for j in range(len(importants) - 1):
    #         if importants[j][0] < importants[j + 1][0]:
    #             importants[j], importants[j + 1] = importants[j + 1], importants[j]
    #
    # for contest in contests:
    #     if contest[1] == 0:
    #         score += contest[0]
    #
    # for index, contest in enumerate(importants):
    #     if index + 1 <= k:
    #         score += contest[0]
    #     else:
    #         score -= contest[0]

    score = sum(i for i, _ in (filter(lambda contest: contest[1] == 0, contests)))

    # from operator import itemgetter
    # data.sort(key=itemgetter(1))

    importants = sorted(list(filter(lambda contest: contest[1] == 1, contests)), key=lambda contest: contests[0],
                        reverse=True)

    print(score)
    print(importants)


luckBalance(3, [(5, 1), (8, 1), (2, 1), (1, 1), (5, 0), (10, 0)])
