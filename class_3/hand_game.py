import random
from string import ascii_lowercase

SCRABBLE_LETTER_VALUES = {
'a' : 1, 'b' : 3, 'c' : 3, 'd' : 2, 'e' : 1, 'f' : 4, 'g' : 2, 'h' : 4, 'i' : 1, 'j' : 8, 'k' : 5, 'l' : 1, 'm' :
3, 'n' : 1, 'o' : 1, 'p' : 3, 'q' : 10, 'r' : 1, 's' : 1, 't' : 1, 'u' : 1, 'v' : 4, 'w' : 4, 'x' : 8, 'y' : 4,
'z' : 10}

def read_words(filename='20k.txt'):
    ''' Read file of most popular English words '''
    with open(filename) as words_file:
        words = words_file.read()
    words = [word for word in words.split('\n') if len(word) > 1]
    return words

def get_word_score(word, hand_size):
    score = 0
    for letter in word:
        score = score + SCRABBLE_LETTER_VALUES[letter]
    score = score * len(word)
    if len(word) == hand_size:
        score = score + 50
    return score

def getFrequencyDict(word):
    hand = {}
    for letter in word:
        if hand.get(letter, 0) != 0:
            hand[letter] = hand[letter] + 1
        else:
            hand[letter] = 1
    return hand

def displayHand(hand):
    word = ""
    for letter in hand.keys():
        for i in range(0, hand[letter]):
            word = word + " " + letter
    print("Current Hand:{}".format(word))

def dealHand(n):
    letters = ''
    for i in range(0, n):
        letters = letters + random.choice(ascii_lowercase)
    return getFrequencyDict(letters)

def updateHand(hand, word):
    new_hand = hand.copy()
    for letter in word:
        new_hand[letter] = new_hand[letter] - 1
    return new_hand

def isValidWord(hand, word):
    validFlag = False
    words = read_words()
    if word in list(words):
        validFlag = True
        for letter in word:
            if hand.get(letter, 0) == 0:
                validFlag = False
                break
    return validFlag

def calculateHandlen(hand):
    len = 0
    for letter in hand.keys():
        len = len + hand[letter]
    return len

def playHand(user_hand, hand_size):
    hand = user_hand.copy()
    handLen = calculateHandlen(hand)
    score = 0
    while handLen > 0:
        displayHand(hand)
        word = input("Enter word, or a '.' to indicate that you are finished: ")
        if word == ".":
            print("Goodbye! Total score: {} points.".format(score))
            break
        if isValidWord(hand, word):
            hand = updateHand(hand, word)
            handLen = calculateHandlen(hand)
            current_score = get_word_score(word, hand_size)
            score = score + current_score
            print("'{0}' earned {1} points. Total: {2} points".format(word,
            current_score, score))
            if handLen == 0:
                print("Run out of letters. Total score: {} points.".format(score))
                break
        else:
            print("Invalid word, please try again.")

def playGame(hand_size):
    inp_string = "\n\nEnter n to deal a new hand, r to replay the last hand, or e to end game: "
    user_choice = input(inp_string)
    hand = {}
    while user_choice != "e":
        if user_choice == "r":
            if hand != {}:
                playHand(hand, hand_size)
            else:
                print("You have not played a hand yet. Please play a new hand first!")
        elif user_choice == "n":
            hand = dealHand(hand_size)
            playHand(hand, hand_size)
        else:
            print("Invalid command.")
        user_choice = input(inp_string)

def main():
    hand_size = 7
    playGame(hand_size)

if __name__ == "__main__":
    main()
