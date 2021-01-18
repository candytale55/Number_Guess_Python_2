# Python 2

"""
Number Guess
This is a console program that rolls a pair of 
dice and asks the user to guess the sum. If the
user's guess is equal to the total value of the
dice roll, the user wins. Otherwise, the computer wins.

Features:
The program should do the following:

* Roll a pair of dice.
* Add the values of the roll.
* Ask the user to guess a number.
* Compare the user's guess to the total value.
* Determine the winner (user or computer).
"""

from random import randint
from time import sleep

#  prompt the user for their guess
def get_user_guess():
  guess = int(raw_input("What's your guess? (number)"))
  return guess


# simulate the rolling of a pair of dice.
def roll_dice(number_of_sides):
  number_of_dice = 2
  max_val = number_of_sides * number_of_dice
  first_roll = randint(1, number_of_sides)
  second_roll= randint(1, number_of_sides)
  total_roll = first_roll + second_roll
  print ("The max possible value is %d" % max_val)
  guess = get_user_guess()
  if guess > max_val:
    print("You number is higher than the maximum possible value %d" %max_val)
  elif guess < 1:
    print ("You number is less than zero. Next time choose a number between 1 and %d" %max_val)
  else:
    print("Rolling ...")
    sleep(2)
    print("First die is %d " %first_roll)
    sleep(1)
    print("Rolling ...")
    sleep(2)
    print("Second die is %d " %second_roll)
    sleep(1)
    print("Result...")
    sleep(1)
    print("Total roll = %s" %total_roll)
    if total_roll == guess:
      print("Your guess was %s " %guess +"too. YOU WON!")
    else: 
      print("Sorry dude, your guess was %s " %guess + "YOU LOST!")


roll_dice(6)

