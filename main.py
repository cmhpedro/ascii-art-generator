import sys
import numpy as np
from ascii import ASCII

text = input()
invalid_chars = []

# check if there is any invalid char
for char in text:
    if char not in ASCII and char not in invalid_chars:
        invalid_chars.append(char)

# exit showing invalid chars if there is any
if invalid_chars:
    print(f"Invalid chars: {invalid_chars}")
    sys.exit(1)

# start art with a column of spaces
art = np.full((12, 1), ' ')

for char in text:
    # delete last column of char that is only space (it's used to scape form '\"' in alphabet.py)
    char_art = np.delete(ASCII[char], -1, 1)

    # overleap art last column with char_art if it's a space
    for i, line in enumerate(art):
        if line[-1] == ' ':
            art[i][-1] = char_art[i][0]

    # add char_art to art, except the first column (already added)
    art = np.concatenate((art, char_art[:, 1:]), axis=1)

# print art
for line in art:
    print(''.join(line))
