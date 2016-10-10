import random

def read_words(filename='20k.txt'):
    ''' Read file of most popular English words '''
    with open(filename) as words_file:
        words = words_file.read()
    words = [word for word in words.split('\n') if len(word) > 5]
    return words


def choose_random_word(words):
    ''' Choose random word from list '''
    return random.choice(words)

def input_letter(available_letters, left_guesses):
    print("You have {} guesses left".format(left_guesses))
    print("Available letters: {}".format(available_letters))
    letter = input("Please guess a letter: ")
    while(letter not in available_letters):
        letter = input("Invalid letter, please try again: ")
    return letter.lower()

def get_word_with_letter(letter, original_word, user_word):
    user_word = list(user_word)
    pos=original_word.find(letter, 0)
    while(pos != -1):
        user_word[pos] = letter
        pos=original_word.find(letter, pos+1)
    return "".join(user_word)

def count_guesses(letter, user_word, left_guesses):
    if(letter in user_word):
        print("Good guess: {}\n".format(user_word))
    else:
        print("Oops! That letter is not in my word: {}\n".format(user_word))
        left_guesses = left_guesses - 1
    return left_guesses

original_word = choose_random_word(read_words()).lower()
user_word = "_" * len(original_word)
available_letters = "abcdefghijklmnopqrstuvwxyz"
left_guesses = 7
print("Welcome to the game, Hangman! \nI am thinking of a word that is "
+ str(len(original_word)) + " letters long.\n")
while((left_guesses > 0) and ('_' in user_word)):
     letter = input_letter(available_letters, left_guesses)
     user_word = get_word_with_letter(letter, original_word, user_word)
     left_guesses = count_guesses(letter, user_word, left_guesses)
     available_letters = available_letters.replace(letter, '')
if(left_guesses > 0):
    print("You won and guessed the word: {}".format(user_word))
else:
    print("Sorry, but you lost. \nThe word I am thinking of is '{}'".format(
    original_word))
