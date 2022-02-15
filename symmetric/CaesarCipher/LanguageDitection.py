ENGLISH_WORDS = []


def get_data ():
	dictionary = open("english_words.txt")
	for word in dictionary.read().split('\n'):
		ENGLISH_WORDS.append(word)
	dictionary.close()
	return ENGLISH_WORDS


def count_words (text):
	text = text.upper()
	words = text.split(' ')
	matches = 0

	for word in words:
		if word in ENGLISH_WORDS:
			matches += 1

	return matches


def is_text_english (text):
	matches = count_words(text)
	if (float(matches) / len(text.split('\n'))) * 100 >= 80:
		return True
	else:
		False


get_data()
text = "akldjkaljslk "
print(is_text_english(text))
