from collections import defaultdict

samples = [(1, 5, 'caaab'), (0, 4, 'xyz'), (2, 4, 'bcdybc')]


def dna_problem(samples):
    gene = ['a', 'b', 'c', 'aa', 'd', 'b']
    health = [1, 2, 3, 4, 5, 6]
    mini = 0
    maxi = 0
    for start, end, input_dna in samples:
        gene_dict = defaultdict(int)

        for index, char in enumerate(gene):
            if index < start:
                continue
            if index > end:
                break
            if gene_dict[char] == 0:
                gene_dict[char] = health[index]
            else:
                gene_dict[char] += health[index]

        # print(dict(gene_dict))

        score = 0
        for begin in range(len(input_dna)):
            for stop in range(1, len(input_dna) + 1):
                end = begin + stop
                if end > len(input_dna):
                    break
                segment = input_dna[begin:end]
                # print(segment)
                score += gene_dict[segment]

        mini = min(score, mini)
        maxi = max(score, maxi)

    return mini, maxi


print(dna_problem(samples))
