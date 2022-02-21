from Crypto.Cipher import DES


# in DES crypto system, we use blocks to encrypt-decrypt, and each block length is 64,
# so the original text should have the length that divisible by 64
# if the length is not divisible by 64, we need to add some special character and make it divisible by 64


def add_padding (text, block_size=64):
	pad_len = block_size - (len(text) % block_size)
	padding = '$' * pad_len
	return text + padding


def remove_padding (string):
	counter = 0

	for c in str[::-1]:
		if c == '$':
			counter += 1
		else:
			break

	return string[:-counter]


def encrypt (plain_text, key):
	des = DES.new(key, DES.MODE_ECB)
	return des.encrypt(plain_text)


def decrypt (cipher_text, key):
	des = DES.new(key, DES.MODE_ECB)
	return des.decrypt(cipher_text).decode('UTF-8')


test_key = 'secretaa'
plain_text_test = 'a test for des encrypto system'

origin_text = add_padding(plain_text_test)
encoded = encrypt(origin_text, test_key)
decoded = decrypt(encoded, test_key)

print(encoded)
print(decoded)
