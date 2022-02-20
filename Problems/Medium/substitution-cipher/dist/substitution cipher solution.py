"""
This encrypted text is so long that I suspect it is the terms and condition of a software.

The flag is in the last line of the correctly recovered plaintext.

Only letters A-Za-z get substituted in the cipher's encryption and decryption operations. All non-letter characters,
including numbers and special characters, are not substituted.
You can additionally use tr command in Linux to iteratively map some characters in the alphabet. For instance,
tr 'hsbtk' ' ETAH' < encrypted.txt, maps 'h' to ' ', 's' to 'E', 'b' to 'T', and so on.
"""
print("\nSubstitution-cipher Question (MEDIUM)")
map = {
    "A": "x",
    "B": "A",
    "C": "x",
    "D": "N",
    "E": "x",
    "F": "H",
    "G": "x",
    "H": "I",
    "I": "x",
    "J": "x",
    "K": "x",
    "L": "O",
    "M": "V",
    "N": "G",
    "O": "F",
    "P": "D",
    "Q": "B",
    "R": "W",
    "S": "x",
    "T": "S",
    "U": "C",
    "V": "x",
    "W": "T",
    "X": "R",
    "Y": "E",
    "Z": "x"
}
from_txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
to_txt = "";
for char in from_txt:
    to_txt += map[char]
print("tr \'" + from_txt + "\' \'" + to_txt + "\' < encrypted.txt")