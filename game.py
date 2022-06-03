import random


def main():
    print("Welcome to the number guessing game!")
    playing = True
    while playing:
        number = random.randint(1, 100)
        tries = 8
        win = play_game(number, tries)
        if win:
            print("You win!")
        else:
            print(f"You lose!, The number was: {number}")
        playing = do_you_want_to_keep_playing()
    print("Bye!")


def play_game(number, tries) -> bool:
    print(f"Guess a number between 1 and 100, You have {tries} tries")
    while tries > 0:
        guess = guess_number()
        if guess == number:
            return True
        elif guess > number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        tries -= 1
    return False


def guess_number() -> int:
    while True:
        try:
            guess = int(input("Guess a number: "))
            return guess
        except ValueError:
            print("Please enter a number")


def do_you_want_to_keep_playing() -> bool:
    while True:
        answer = input("Do you want to play again? (y/n) ")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please enter y or n")


if __name__ == "__main__":
    main()
