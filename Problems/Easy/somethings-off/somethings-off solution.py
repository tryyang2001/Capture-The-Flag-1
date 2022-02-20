print("Something's off Question")
cipher = "QgGFEL{JvFt7_qF3vH56_I5H_I_ufM_AI5a8d}"
plain = "CS2107"
mapping = {
    "E" : "0",  #confirmed
    "F" : "1",  #confirmed
    "G" : "2",  #confirmed
    "H" : "3",
    "I" : "4",
    "J" : "5",
    "K" : "6",
    "L" : "7",  #confirmed
    "M" : "8",
    "N" : "9",
    "o" : "a",
    "p" : "b",
    "q" : "c",
    "r" : "d",
    "s" : "e",
    "t" : "f",
    "u" : "g",
    "v" : "h",
    "w" : "i",
    "x" : "j",
    "y" : "k",
    "z" : "l",
    "0" : "m",
    "1" : "n",
    "2" : "o",
    "3" : "p",
    "4" : "q",
    "5" : "r",
    "6" : "s",
    "7" : "t",
    "8" : "u",
    "9" : "v",
    "A" : "w",
    "B" : "x",
    "C" : "y",
    "D" : "z",
    "O" : "A",
    "P" : "B",
    "Q" : "C",  #confirmed
    "R" : "D",
    "S" : "E",
    "T" : "F",
    "U" : "G",
    "V" : "H",
    "W" : "I",
    "X" : "J",
    "Y" : "K",
    "Z" : "L",
    "a" : "M",
    "b" : "N",
    "c" : "O",
    "d" : "P",
    "e" : "Q",
    "f" : "R",
    "g" : "S",  #confirmed
    "h" : "T",
    "i" : "U",
    "j" : "V",
    "k" : "W",
    "l" : "X",
    "m" : "Y",
    "n" : "Z"
}

def translate(cipher):
    plain = ""
    for char in cipher:
        if (char == '_' or char == '{' or char == '}'):
            plain = plain + str(char)
        else:
            plain = plain + mapping[char]
    return plain

print(translate(cipher))