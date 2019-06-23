string = 'rrrryyer '
string = string.strip()
string_list = list(string)
string_list.reverse()

output = [string_list[0], '1']
done = string_list[0]
for char in string_list[1:]:
    if char.isalnum():
        if char == done:
            count = int(output.pop())
            output.append(str(count+1))
        else:

            done = char
            output.extend([char, '1'])

output.reverse()
print("".join(output))