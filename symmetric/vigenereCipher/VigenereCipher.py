ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def vigenere_encrypt (plain_text, key):
	plain_text = plain_text.upper()
	key = key.upper()

	cipher_text = ''

	# since, vigenere cipher uses iteration logic on the key, we need iterate it several times
	current_key_index = 0

	for character in plain_text:
		index = ALPHABET.find(character)
		if index != -1:
			valid_index = (index + ALPHABET.find(key[current_key_index])) % len(ALPHABET)
			cipher_text = cipher_text + ALPHABET[valid_index]
			current_key_index = (current_key_index + 1) % len(key)
		else:
			cipher_text = cipher_text + '.'

	return cipher_text


def vigenere_decrypt (cipher_text, key):
	cipher_text = cipher_text.upper()
	key = key.upper()

	plain_text = ''

	# since, vigenere cipher uses iteration logic on the key, we need iterate it several times
	current_key_index = 0

	for character in cipher_text:
		index = ALPHABET.find(character)
		if index != -1:
			valid_index = (index - ALPHABET.find(key[current_key_index]) + len(ALPHABET)) % len(ALPHABET)
			plain_text = plain_text + ALPHABET[valid_index]
			current_key_index = (current_key_index + 1) % len(key)
		else:
			plain_text = plain_text + '.'

	return plain_text


encoded = vigenere_encrypt("I'm an uyghur", "adil")
decoded = vigenere_decrypt(encoded, 'adil')
print(encoded)
print(decoded)
