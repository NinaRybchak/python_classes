def is_vowel(char):
	return char.lower() in 'aeiou'

char = input("Char is: ")
print("Is a char vowel? - {}".format(is_vowel(char)))
