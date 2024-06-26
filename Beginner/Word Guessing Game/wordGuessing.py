import random
print("Good Luck !\n\n")
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
answer = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 12
# the number of turns should become dependant on the randomly chosen word
# yet to implement
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print(f"You Win \nThe word is: {answer}")
        break
    guess = input("\n guess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print(f"Wrong \n You have {turns} more guesses")
        if not turns: print("You Loose")
