"""
this is a number guessing game game 
"""
#imports
import random
import math

#inputs
maxNum = int(input("Enter max number:\n"))
minNum = int(input("Enter min number:\n"))

#randomly chosen number
Answer = random.randint(minNum,maxNum)

# minimum number of guesses is the (Log 2 of maxNum - minNum ) + 1
Lifes = int(math.log(maxNum - minNum,2)) + 1
print(f'you have {Lifes} guesses')
for i in range (Lifes):
  guess = int(input('Guess a number: \n'))
  if guess > Answer:
    print("You Guessed too high!")
  elif guess < Answer:
    print("You guessed too small!")
  else:
    print(f"Congratulations you did it in {i+1} tries")
    break
else:
  print(f'You failed the right answer is "{Answer}" .better luck next time')
#this line below is for keeping the terminal until exiting
input('press any key to exit')
