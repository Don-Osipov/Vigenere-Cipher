# !/usr/bin/python
import sys

print(sys.argv)
if len(sys.argv) < 4:
    print('usage: ARGS="encode/decode plaintext/ciphertext keyword')
    sys.exit()


whatToDo = sys.argv[1]
encodeOrDecode = True
text = sys.argv[2].upper()
keyword = sys.argv[3].upper()

letterToNum = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
}
numToLetter = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    25: "Z",
}

if whatToDo == "encode":
    encodeOrDecode = True
elif whatToDo == "decode":
    encodeOrDecode = False


def preProcessing(text):
    replaceDict = {" ": "", ",": "", ".": "", "!": "", "?": ""}
    for before, after in replaceDict.items():
        text = text.replace(before, after)
    return text


def elongateKeyword(keyword, plaintext):
    targetLength = len(plaintext)
    keyText = ""

    while len(keyText) < targetLength:
        for letter in keyword:
            keyText += letter
            if len(keyText) >= targetLength:
                break

    return keyText


# num = letterToNum["E"]
# num2 = letterToNum["Y"]
# print(numToLetter[(num + num2) % 26])


# def encypt(plaintext, keyText):
#     cipherText = ""

#     if len(plaintext) != len(keyText):
#         keyText = elongateKeyword(keyText, plaintext)

#     for letter, key in zip(plaintext, keyText):
#         letterNum = letterToNum[letter]
#         keyNum = letterToNum[key]
#         encryptedLetter = numToLetter[(letterNum + keyNum) % 26]
#         cipherText += encryptedLetter

#     return cipherText


def vigenere(text, key, encrypt: bool):
    text = preProcessing(text)
    key = preProcessing(key)

    newText = ""

    if len(text) != len(key):
        key = elongateKeyword(key, text)

    if encrypt:
        for letter, key in zip(text, key):
            letterNum = letterToNum[letter]
            keyNum = letterToNum[key]

            newLetter = numToLetter[(letterNum + keyNum) % 26]
            newText += newLetter
        return newText
    else:
        for letter, key in zip(text, key):
            letterNum = letterToNum[letter]
            keyNum = letterToNum[key]

            newLetter = numToLetter[(letterNum - keyNum + 52) % 26]
            newText += newLetter
        return newText


print("\nresult: " + vigenere(text, keyword, encodeOrDecode))

# print(encypt(plaintext, keyword))

