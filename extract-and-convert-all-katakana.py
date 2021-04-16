import json
alphabet = list(map(str, 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤ－ユ－ヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポャュョァィェォュ'))
words = []
with open('raw_words.json') as f:
    raw_data = json.load(f)
for block in raw_data:
    words.append(str(block[0]))

alphabet_words = []
for word in words:
    for letter in word:
        if letter in alphabet:
            alphabet_words.append(word)

with open('all_katakana_word_list.txt', 'x') as f:
    for word in alphabet_words:
        f.write("%s\n" % word)
