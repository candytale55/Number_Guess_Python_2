# Number_Guess_Python_2

## General info
This is a console program that rolls a pair of  dice and asks the user to guess the sum. If the user's guess is equal to the total value of the dice roll, the user wins. Otherwise, the computer wins.

## Features
The program should do the following:

* Roll a pair of dice.
* Add the values of the roll.
* Ask the user to guess a number.
* Compare the user's guess to the total value.
* Determine the winner (user or computer).

### More info:

To make sure that the rolls are random we imported the _randint_ function from the _random_ module.

To simulate dice rolls: we imported the _sleep_ function from the _time_ module to sleep the program for 2 seconds to simulate the dice rolling.

**_get_user_guess()_** :  prompt the user for their guess

**_roll_dice(number_of_sides)_** : used to simulate the rolling of a pair of dice. A single die can land on any value that’s at least 1 and no greater than the die's number of sides. The _randint_ functions generates a random integer between 1 and number_of_sides. _max_val_ calculates the maximum value the program can possibly roll, which is the number_of_sides times the _number_of_dice.

## Table of contents
* [General info](#general-info)
* [Features](#features)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)
* [References](#references)


## Screenshots
![Example screenshot](./img/screenshot.png)

## Technologies
* Python 2 - Probably will also work for Python 3

## Setup
NA

## Status
Project is:  _finished_

## References
From course _Learn Python 2_ here: https://www.codecademy.com/learn/learn-python
