import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                if (number_to_guess-guess>=6):
                    print("Too low! Try again.")
                else:
                    print("low,but close")
            elif guess > number_to_guess:
                if (guess-number_to_guess>=6):
                    print("Too high! Try again.")
                else:
                    print("High,but close")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
                print(f"It took you {attempts} attempts.")
                print("Your score is ",(100/attempts))
                guessed = True
        except ValueError:
            print("Please enter a valid number.")
        
            
# Run the game
number_guessing_game()
 
