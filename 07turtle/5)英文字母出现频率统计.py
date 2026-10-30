sentense=input("输入一段英文")
letter_count = {}
for letter in sentense:
    if letter.isalpha():
        letter = letter.lower()
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

for letter, count in sorted(letter_count.items()):
    print(f"{letter}: {count}")
letter_count = []

for letter in sentense:
    if letter.isalpha():
        letter = letter.lower()

        for item in letter_count:
            if item[0] == letter:
                item[1] += 1
                break
        else:
            letter_count.append([letter, 1])

letter_count.sort(key=lambda item: item[1], reverse=True)

for letter, count in letter_count:
    print(f"{letter}: {count}")