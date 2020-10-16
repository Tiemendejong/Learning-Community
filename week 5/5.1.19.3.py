word = input("Which word?")
count = 0
answer = input("Which letter?")
for letter in word:
    if letter == answer:
        count += 1
print(count)
