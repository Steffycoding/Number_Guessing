import random

# User guessing the number
def user_guess(x):
    # Generate a random number between 1 and x
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        # Get user input for the guess
        print(f'NOW IT IS YOUR TURN TO GUESS YOUR NUMBER...')
        guess = int(input(f'Guess a number between 1 and {x}: '))
        # Check if the guess is too low or too high
        if guess < random_number:
            print('Sorry, guess again. Too low')
        elif guess > random_number:
            print('Sorry, guess again. Too high')
    # Print a congratulatory message
    print(f'Yay, congrats. You have guessed the number {random_number} correctly.')

# Computer guessing with different strategies

# Strategy 1: Always guesses in the middle
def computer_guess_easy(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        # Guess a random number between the current range
        guess = random.randint(low, high)
        # Get user feedback on the guess
        print(f'NOW IT IS THE COMPUTERS TURN TO GUESS YOUR NUMBER...')
        feedback = input(f'Is {guess} the correct number? (Y/N): ').lower()
        # Adjust the range based on user feedback
        if feedback == 'n':
            if guess > x // 2:
                print('Too high! Try a lower number.')
                high = guess - 1
            else:
                print('Too low! Try a higher number.')
                low = guess + 1
        elif feedback == 'y':  # Added this condition
            print(f'Yay! The computer guessed your number, {guess}, correctly!')
            break  # Exit the loop when 'y' is entered
    # # Print a congratulatory message (moved outside the loop)
    # print(f'Yay! The computer guessed your number, {guess}, correctly!')


# Strategy 2: Randomly decides whether to guess higher or lower than the middle
def computer_guess_hard(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        # Guess a random number between the current range
        guess = random.randint(low, high)
        # Get user feedback on the guess
        print(f'NOW IT IS THE COMPUTERS TURN TO GUESS YOUR NUMBER...')
        feedback = input(f'Is {guess} the correct number? (Y/N): ').lower()
        # Adjust the range based on user feedback using random choice
        if feedback == 'n':
            if random.choice([True, False]):
                print('Too high! Try a lower number.')
                high = guess - 1
            else:
                print('Too low! Try a higher number.')
                low = guess + 1
    # Print a congratulatory message
    print(f'Yay! The computer guessed your number, {guess}, correctly!')

# Strategy 3: Always guesses the exact middle of the current range
def computer_guess_smart(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        # Guess the middle number of the current range
        guess = (low + high) // 2
        # Get user feedback on the guess
        feedback = input(f'Is {guess} the correct number? (Y/N): ').lower()
        # Adjust the range based on user feedback
        if feedback == 'n':
            if guess > x // 2:
                print('Too high! Try a lower number.')
                high = guess - 1
            else:
                print('Too low! Try a higher number.')
                low = guess + 1
    # Print a congratulatory message
    print(f'Yay! The computer guessed your number, {guess}, correctly!')

# User guessing the number with a range of 20
user_guess(20)

# Computer guessing with different strategies and different ranges
computer_guess_easy(30)
computer_guess_hard(25)
computer_guess_smart(50)
