import random
def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 3
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")

    while attempts<max_attempts:
        guess = int(input("Enter your guess: "))
        attempts= +1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number}.")
