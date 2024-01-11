# 10.1.2024
# A friend mentioned in an email he'd coded a version of Wordle. I could not resist having a go too.

# Leaving this for now: basic functionality is there. Things to fix include:
# -- If a letter appears twice in a guess, BOTH are counted 'yellow' even if the letter appears only once in the word


import random

                            # This is just ASCII so symbols to replace colours will have to do for now
grey = "X"
yellow = "^"
green = "█"

wordlist = ["foxes","beard","satan","flock","twist","habit","newts"]

                            # returns False if it's not valid; returns the word in capital letters if it is
def is_valid(word):
    if len(word) != 5:
        return False
    for letter in word:
        if not is_letter(letter):
            return False
    return capitalize(word)

def capitalize(word):
    capword = ""
    for letter in word:
        if ord(letter) > 96:
            capletter = chr(ord(letter)-32)
        capword += capletter
    return capword

def is_letter(char):
    if ord(char) < 65 or ord(char) > 90:
        if ord(char) < 97 or ord(char) > 122:
            return False
    return True


def wordle(word):
    print(grey + " -- letter doesn't appear in the word")
    print(yellow + " -- letter is in the word, but not here")
    print(green + " -- right letter, right place!")
    word = is_valid(word)
    if not word:
        return

    guesses = get_guesses(word)

                            # (function returns 0 if word isn't guessed)
    if guesses > 0:
        print(str(guesses) + "/6")
    else:
        print ("X/6")

                            # Gets, responds to, and counts guesses from player
def get_guesses(word):
    for turns in range (6):
        guess = input("It's your turn: ")
        guess = is_valid(guess)
        if not guess:
            return
        print(hints(word, guess))
        if guess == word:

            return turns+1
    return 0


def hints(word,guess):
    hints = ["","","","",""]
                            # Greys first
    for index in range(0,len(guess)):
        if word.count(guess[index]) == 0:
            hints[index] = grey
                            # Yellows
    for index in range(0,len(guess)):
        if word.count(guess[index]) > 0:
            hints[index] = yellow
    for index in range(0,len(guess)):
        if word.count(guess[index]) > 0 and guess[index] == word[index]:
            hints[index] = green

    output_hints = ''.join(map(str, hints))
    return(guess + "\n" + output_hints)



if __name__ == "__main__":
    choice = random.randint(0,len(wordlist)-1)
    word = wordlist[choice]
    wordle(word)