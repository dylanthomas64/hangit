__author__ = 'Dylan'
# HANG MAN GAME

from random import randint

'''def getAnswer():
    correct = -1
    for letter in noun:
        if inputLetter == letter:
            if answer[noun.index(letter)] != letter:
                answer[noun.index(letter)] = letter
                correct = 1
            else:
                correct = 0
        elif inputLetter in wrongLetters:
            correct = 0
        else:a
            pass
    if correct == 1:
        return 1
    elif correct == -1:
        return -1
    elif correct == 0:
        return 0'''


def _get_answer():
    if inputLetter in lettersList:
        if inputLetter in wrongLetters:
            return 0
        elif inputLetter in answer:
            return 0
        else:
            counter = 0
            for letter in lettersList:
                if letter == inputLetter:
                    answer[lettersList.index(letter, counter)] = letter
                    counter += (lettersList.index(letter)) + 1
                else:
                    continue
            return 1
    else:
        if inputLetter in wrongLetters:
            return 0
        elif inputLetter in answer:
            return 0
        else:
            return -1


while True:
    # CREATE WORD
    nounFile = open("List of Nouns.txt", "r")
    nounList = []
    numberOfNouns = -1
    for line in nounFile:
        nounList.append(line)
        numberOfNouns += 1
    noun = nounList[randint(1, numberOfNouns)]
    lettersList = list(noun)
    del lettersList[-1]
    nounFile.close()

    # CREATE ANSWER BLOCK E.G. _ /_ /_ /_ /_
    answer = []
    for x in lettersList:
        answer += "_"

    wrongLetters = []
    tries = 0

    print("You will only be given 10 incorrect guesses to complete the word.\nLet's play Hang Man!\n\n")
    print(" / ".join(answer))

    while tries <= 10:
        try:
            inputLetter = input("\n--> ").lower()
            if not inputLetter.isalpha():
                raise ValueError
            elif len(inputLetter) != 1:
                raise ValueError
            else:
                result = _get_answer()
                if result == 1:
                    print("Well done...\t", " / ".join(answer))
                    print("\nWrong letters: ", wrongLetters)
                elif result == -1:
                    wrongLetters += inputLetter
                    print("Sorry...\t", " / ".join(answer))
                    print("\nWrong letters: ", wrongLetters)
                    tries += 1
                elif result == 0:
                    # TODO Must remember to fix
                    print("You've already tried that letter!")
            if answer == lettersList:
                print("Congratulations!! You win!!")
                break
            else:
                print("You have", 10 - tries, "wrong answers left.")
        except ValueError:
            # TODO Come up with error message
            print("Please type in a single valid letter!")
    if answer != lettersList:
        print("\nYou've run out of tries!! Better luck next time...")
        print("The correct answer was", ("".join(lettersList)).upper())
    if input("\nWould you like to play again? ") not in ("n", "no", "nah", "nope", "nay", "narp"):
        continue
    else:
        break
exit()
