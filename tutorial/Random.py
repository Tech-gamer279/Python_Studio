"""
==========================================
Random Number Game Tutorial
==========================================

This tutorial demonstrates how to create a simple random number guessing game in Python using the `random` library.

------------------------------------------
1. Import the random Library
------------------------------------------
    import random

------------------------------------------
2. Generate a Random Number
------------------------------------------
    secret_number = random.randint(1, 10)  # Random number between 1 and 10

------------------------------------------
3. Get User Input and Compare
------------------------------------------
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("Congratulations! You guessed it right.")
    else:
        print("Sorry, the correct number was", secret_number)

------------------------------------------
4. Full Example
------------------------------------------
"""

import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Congratulations! You guessed it right.")
else:
    print("Sorry, the correct number was", secret_number)

"""
------------------------------------------
5. Tips
------------------------------------------
- You can use a loop to let the user guess multiple times.
- Use exception handling to manage invalid input.

For more information, see the official docs:
https://docs.python.org/3/library/random.html
"""