
import random as rd

# Function to return a random number
def Random_number():
    number = rd.randrange(1, 100, 1)
    return number

# Function to greet the user to play the game
def greeting():
    text = """
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    You have as many chances as you selected difficulty.
    """
    return text

print(greeting())


while True:
    chances = 0
    tries = 1  # always 1 counting the first game and the first attempt
    # Select the option and the level is always easy to start
    print("Please select your difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
    option = int(input())
    if option == 1:
        chances = 10
        print(f"Great! You selected the Easy difficulty level.")
        print("Let's start the game!")
    elif option == 2:
        chances = 5
        print(f"Great! You selected the Medium difficulty level.")
        print("Let's start the game!")
    elif option == 3:
        chances = 3
        print(f"Great! You selected the Hard difficulty level.")
        print("Let's start the game!")
    else:
        print("This option doesn't exist!")
        continue  # Ask for the option again

    guess_number = Random_number()
    
    while chances != 0:
        user_try = int(input("Enter your choice:\n"))
        if user_try < guess_number:
            print("Not yet! The number is greater than {}".format(user_try))
            tries += 1 
            chances -= 1
        elif user_try > guess_number:
            print("Not yet! The number is less than {}".format(user_try))
            tries += 1
            chances -= 1
        else:
            print("Congratulations! You guessed the correct number in {} attempts.".format(tries))
            break  # Exit the guessing loop if the correct number is guessed

    if chances == 0:
        print("Sorry, you are out of chances the number was {}".format(guess_number))
    
    exit = input("Do you want to quit the game? (y/n): ")
    if exit.lower() == 'y':
        break  # Exit the main loop if the user wants to quit
