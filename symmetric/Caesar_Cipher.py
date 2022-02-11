ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY = 100


# this algorithm uses index of each letter and adding a key value to the index
# so that plain text has been en and decrypted


def caesar_crypto(text, target):
    global KEY
    result = ""
    if target == "de":
        KEY = -KEY
    for c in text.upper():
        index = ALPHABET.find(c)
        result += c if index == -1 else ALPHABET[(index + KEY) % 26]
    return result


print(caesar_crypto(caesar_crypto("men bir uyghur!!", "en"), "de"))

print(caesar_crypto("hello to crypto world!","en"))

# TODO: convert to JAVA
