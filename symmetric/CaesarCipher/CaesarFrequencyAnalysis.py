import matplotlib.pylab as plt

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
testCipher = "WKLVCLVCWKHCEHJLQQLQJCRICDCVHFUHWC RUOGC KHUHCILQGLQJCRXWCLVCDO DBVCFRQVLGHUHGCDQCLPSRVVLEOHCWDVN,CEXWCVXFFHVVCLVC KHUHCWKHCWUXWKCOLHV!"


def frequency_analysis(text):
    text = text.upper()
    letters_frequencies = {}

    for letter in ALPHABET:
        letters_frequencies[letter] = 0

    for letter in text:
        if letter in ALPHABET:
            letters_frequencies[letter] += 1

    return letters_frequencies


def plot_distribution(cipher):
    frequencies = frequency_analysis(cipher)
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()


plot_distribution(testCipher)

# most frequent letters in english: Desc: e (a,i,o,t)
