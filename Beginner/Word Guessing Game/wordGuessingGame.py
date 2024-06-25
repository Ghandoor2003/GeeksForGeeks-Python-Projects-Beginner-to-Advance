"""
This is a word guessing game similar to hanged man
"""
import random
def readCh(txt="guess a character:\n"):
  ch = input(txt).lower()
  if len(ch) == 1 and ch.isalpha():
    if ch not in guessedChrs:
      return ch
    else:
      return readCh(txt="you have already guessed this character, guess another : \n")
  else:
    return readCh(txt="you can choose only a single alphabetical character, guess another :\n")

words = ['answer' , 'solution' , 'eeeaeee']
answer = random.choice(words)
lifes = 7
guessedChrs = []

while 1:
  guess = readCh()
  if guess in answer:
    guessedChrs.append(guess)
  else :
    lifes -= 1
  T = ''
  for i in answer:
    if i in guessedChrs:
      T += i
    else:
      T += '_'
  print(T)
  if T == answer:
    print('congratulations')
    break
  if lifes == 0:
    print(f'you lost , the true answer is {answer}')
    break
  print(f'you have {lifes} lifes yet')
input('press any to exit')
