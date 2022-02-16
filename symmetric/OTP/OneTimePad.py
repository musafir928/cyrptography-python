from random import randint

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt (plain_text, key):
	plain_text = plain_text.upper()
	cipher_text = ''

	for index, char in enumerate(plain_text):
		key_index = key[index]
		char_index = ALPHABET.find(char)
		if char_index != -1:
			cipher_text += ALPHABET[(char_index + key_index) % len(ALPHABET)]
		else:
			cipher_text += char

	return cipher_text


def decrypt (cipher_text, key):
	cipher_text = cipher_text.upper()
	plain_text = ''

	for index, char in enumerate(cipher_text):
		key_index = key[index]
		char_index = ALPHABET.find(char)
		if char_index != -1:
			plain_text += ALPHABET[(char_index - key_index + len(ALPHABET)) % len(ALPHABET)]
		else:
			plain_text += char

	return plain_text


def random_sequence (plain_text):
	random = []

	for _ in range(len(text)):
		random.append(randint(0, len(ALPHABET) - 1))

	return random


if __name__ == "__main__":
	text = "This is a test for random function"
	random_numbers = random_sequence(text)
	encoded = encrypt(text, random_numbers)
	decoded = decrypt(encoded, random_numbers)
	print(text)
	print(random_numbers)
	print(encoded)
	print(decoded)
