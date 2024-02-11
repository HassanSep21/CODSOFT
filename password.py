from random import randint
from string import ascii_letters, punctuation, digits


def main():
    while True:
        try:
            length = int(input("Enter password length: "))
            print("Your Password: ", end="")
            password(length)
            break
        except ValueError:
            print("INVALID INPUT")


# Generates and Prints Password
def password(length):
    key = ascii_letters + punctuation + digits
    password = []

    while length != 0:
        password += key[randint(0, len(key) - 1)]
        length -= 1

    for char in password:
        print(char, end="")
    print()


if __name__ == "__main__":
    main()