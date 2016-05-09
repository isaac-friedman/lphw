def break_words(stuff):
	"""breaks stuff into words by spaces"""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words alphabetically"""
	return sorted(words)

def print_first_word(words):
	"""Pops and prints the first word.
	words -- a list of words obtained from break_words(stuff)

	By the way, this is the appropriate format for a multiline docstring.
	You've now learned two terms: docstring and pop. Google them.
	"""
	first_word = words.pop(0)
	print first_word

def print_last_word(words):
	"""Prints the last element of words"""
	last_word = words.pop(-1)
	print last_word
	
def sort_sentence(sentence):
	"""Takes a sentence, breaks it into words and sorts the words"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""prints the first and last words of the sentence
	Bonus question: why could this function name be confusing in this
	context? Can you think of a better one?
	"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts all the words in sentence and then prints the first and last"""
	words = break_words(sentence)
	sort_words(words)
	print_first_word(words)
	print_last_word(words)
