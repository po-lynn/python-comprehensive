# import random

# # List of words to choose from
# words = ['apple', 'banana', 'orange', 'mango']

# # Choose a random word
# word = random.choice(words)

# # Print the word, along with a message
# print(f"The chosen word is: {word}")

# # Set the number of guesses to 0
# num_guesses = 0

# # Set the maximum number of guesses allowed
# max_guesses = 5

# # Set the game to not yet won
# game_won = False

# # Keep playing until the game is won or the user runs out of guesses
# while not game_won and num_guesses < max_guesses:
#     # Get the user's guess
#     guess = input("Enter your guess: ")

#     # Check if the guess is correct
#     if guess == word:
#         game_won = True
#         print("Correct! You guessed the word.")
#     else:
#         print("Incorrect. Try again.")
#         num_guesses += 1

# # If the game was not won, print the correct word
# if not game_won:
#     print("You ran out of guesses. The correct word was:", word)

''' DIce '''
# from random import randint
# # Roll the dice
# result = randint(1, 6)
# print(f"You rolled a {result}")

"HEAD Tails"
# import random

# coin = random.choice(["heads","tails"])
# print(coin)

# import random

# cards = ["jack","queen","king"]
# random.shuffle(cards)
# print(cards)


import sys

# print("Hello, my name is ", sys.argv[1])
# try:
#     print("Hello, my name is ", sys.argv[1])
# except IndexError:
#     print("Too few arguments")
# 

# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello, my name is ", sys.argv[1])

# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")

# print("Hello, my name is ", sys.argv[1])

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
    
# print("Hello, my name is ", sys.argv[1])

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# for arg in sys.argv[1:]:
#     print("hello my name is ", arg)

import cowsay
import sys

if len(sys.argv) ==2:
    cowsay.trex("hello", sys.argv[1])
cowsay.dragon('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris blandit rhoncus nibh. Mauris mi mauris, molestie vel metus sit amet, aliquam vulputate nibh.')

cowsay.cow('Hello World')