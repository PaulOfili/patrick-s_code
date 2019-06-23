erica = 'EEMEE'
bob = 'EESSH'

erica_levels = [0, 0, 0]
bob_levels = [0, 0, 0]

erica_score = 0
bob_score = 0

for erica_char, bob_char in zip(erica, bob):
    if erica_char == 'E':
        erica_levels[2] += 1
        erica_score += 1
    if bob_char == 'E':
        bob_levels[2] += 1
        bob_score += 1
    if erica_char == 'M':
        erica_levels[1] += 1
        erica_score += 3
    if bob_char == 'M':
        bob_levels[1] += 1
        bob_score += 3
    if erica_char == 'H':
        erica_levels[0] += 1
        erica_score += 5
    if bob_char == 'H':
        bob_levels[0] += 1
        bob_score += 5

print(erica_score, erica_levels, bob_score, bob_levels)

if erica_score > bob_score:
    print("ERICA")
elif bob_score > erica_score:
    print("BOB")
else:
    for erica_lev, bob_lev in zip(erica_levels, bob_levels):
        if erica_levels > bob_levels:
            print("ERICA")
            break
        elif erica_levels < bob_levels:
            print("BOB")
            break
    else:
        print('TIE')
