from random import randint
from sys import exit
from os import system

# Win Posibilities
pairs = [[False, False, True],
         [True, False, False],
         [False, True, False]]

# Score Counter
score = 0


def main():
    while True:
        try:
            system("clear")
            print(f"SCORE: {score}")
            print("1. Rock 🪨\n2. Paper 📃\n3. Scissors ✂️")
            print("-* Press [Q] to Quit *-") 
            choice = input("Choice (Digits): ")
            if choice.capitalize() == "Q":
                exit("-* Thanks For Playing *-")
            elif 0 < int(choice) < 4:
                print(winner(int(choice) - 1))
            else:
                print("INVALID INPUT")

        except (ValueError, IndexError):
            continue

        ask = input("New Round? [Y/N]: ").capitalize()
        if ask != "Y":
            exit()


# Computer's Choice
def computerChoice():
    choice = randint(0, 2)
    if choice == 0:
        print("Computer chose Rock 🪨")
    elif choice == 1:
        print("Computer chose Paper 📃")
    else:
        print("Computer chose Scissors ✂️")
    return choice


# Checking for Winner
def winner(choice):
    comp = computerChoice()
    if comp == choice:
        return "-* Tie *-"
    elif pairs[choice][comp] == True:
        global score
        score += 1
        return "-* You Win *-"
    else:
        return "-* You Lose *-"


if __name__ == "__main__":
    main()
