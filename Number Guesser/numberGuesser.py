import art
import random
print(art.logo)


def compare(n1, n2):
    if n1 > n2:
        return "Too High"
    elif n1 < n2:
        return "Too low"
    else:
        return "You won!"


def resultGiver(attempt):
    computerGuess = random.randint(1, 100)
    while attempt:
        print(f"You have {attempt} attempts left.")
        userValue = int(input("Make a guess: "))
        result = compare(userValue, computerGuess)
        print(result)
        if result == "You won!":
            break
        attempt -= 1
        if attempt == 0:
            print("You lost!")
            print(f"Computer's guess was {computerGuess}")

def numberGuesserGame():
    attempts = 10
    print("Welcome to the Number Guesser Game!")
    print("I'm thinking of a number between 1 and 100.")
    userInput = input("Choose a difficulty. Type 'easy' or 'hard' to play: ")
    if userInput == 'easy':
        resultGiver(attempts)
    elif userInput == 'hard':
        attempts = 5
        resultGiver(attempts)


numberGuesserGame()