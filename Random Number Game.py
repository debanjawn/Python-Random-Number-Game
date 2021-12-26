#the computer will generate random number from 0-100, the user is offered 7 guesses in effort to find that number, when the user guesses wrong it will tell the user if too high or low, and when user guesses correcty the game is won
from random import randint
attempt = 0
while(attempt <= 7):
  attempt = attempt + 1
  rNum = randint(0,100)
  uGuess = int(input('Guess a number from 0 to 100 ') )
  if rNum < uGuess:
    print('Ur Guessed Number is greater than the Number')

  elif rNum > uGuess:
    print('Ur Guessed Number is less than the Number')

  else:
    print('Congratz, You got it!')
    attempt = 9 
50