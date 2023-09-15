import random

def play_guessing_game():
    print("Welcome to the Guessing Game!")
    play_again = True
    total_attempts = 0
    total_rounds = 0

    while play_again:
        lower_limit = 1
        upper_limit = 100
        secret_number = random.randint(lower_limit, upper_limit)
        attempts = 0
        correct_guess = False
        total_rounds += 1

        print(f"\nRound {total_rounds}")
        print(f"Guess the number between {lower_limit} and {upper_limit}")

        max_attempts = 7  # You can change this to limit the number of attempts per round

        while attempts < max_attempts:
            try:
                user_guess = int(input("Enter your guess: "))
            except ValueError:5
            
                print("Please enter a valid number.")
                continue

            attempts += 1
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                correct_guess = True
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break

        if not correct_guess:
            print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")

        total_attempts += attempts
        play_again = input("Do you want to play again? (yes/no): ").lower().startswith('y')

    print(f"\nGame Over!")
    print(f"Total Rounds Played: {total_rounds}")
    print(f"Total Attempts: {total_attempts}")
    print(f"Average Attempts per Round: {total_attempts / total_rounds:.2f}")

if __name__ == "__main__":
    play_guessing_game()
