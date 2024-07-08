import random

while True:
    number = random.randint(1, 10)
    guess = int(input("Silly game! Guess a number between 1 and 10: "))

    if guess == number:
        print("You Won!")
    else:
        print("removing...(C:\\Windows\\System32)")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break

print("Thanks for playing!")
    