def is_vowel(char):
	if(char.lower() in "aeiou"):
		return True
	else:
		return False

char = input("Char is: ")
print("Is a char vowel? - {}".format(is_vowel(char)))
