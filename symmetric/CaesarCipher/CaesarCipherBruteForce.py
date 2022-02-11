# the goal is to decode the Caesar cipher
ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_crypto(text, target, KEY):
    result = ""
    if target == "de":
        KEY = -KEY
    for c in text.upper():
        index = ALPHABET.find(c)
        result += c if index == -1 else ALPHABET[(index + KEY) % 26]
    return result


def decode_caesar(text):
    for i in range(len(ALPHABET)):
        print(f"the result for key {i} is: {caesar_crypto(text, 'de', i)}")


decode_caesar("LIPPSDXSDGVCTXSDASVPH!")
# the result is:
# the result for key 4 is: HELLO TO CRYPTO WORLD!
# this solution works for caesar cause limitation of key value which is only 27 (0~26)