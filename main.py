with open('books/frankenstein.txt') as f:
    file_contents = f.read()

alphabet = {}

words = file_contents.split()

for w in words:
    for l in w:
        if l.isalpha():
            letter = l.lower()
            try:
                alphabet[letter] += 1
            except KeyError:
                alphabet[letter] = 1

liste = list(alphabet.items())
liste = sorted(liste,key=lambda letter: letter[1])
for l in liste:
    print(f"The letter {l[0]} appeared {l[1]} times")
