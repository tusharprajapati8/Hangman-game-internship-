import random

words = ["computer ","python","apple","game"]
word = random.choice(words)

guessed = ""
chance = 6

print("welcome to Hangman game")

while chance > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("word:", display)

    if display == word:
       print("Congratulations! you won")
       break

    guess = input("Enter a letter: ")

    if guess in word:
                guessed += guess
                print("Correct guess!")

    else:
        chance -=1
        print("Wrong guess!")
        print("Chances left:", chance)

print("game over" if chance == 0 else "game finished")

if chance ==0:
    print("the word was:", word)