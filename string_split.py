sample = "I  am a boy"
array = [""] * (sample.count(" ") + 1)

index = 0
for char in sample:
    if char is not " ":
        array[index] += char
    else:
        index += 1

print(array)
print(sample.split(" "))