import json
alphabet = list(map(str, 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤ－ユ－ヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポャュョァィェォュ'))
words = []
with open('raw_words.json') as f:
    raw_data = json.load(f)
for block in raw_data:
    words.append(str(block[0]))

alphabet_words = []
for word in words:
    contains_another = False
    for letter in word:
        if letter not in alphabet:
            contains_another = True
    if contains_another == False:
        alphabet_words.append(word)

with open('word_list.txt', 'x') as f:
    for word in alphabet_words:
        f.write("%s\n" % word)
