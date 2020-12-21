# Number randomly generated 
# Give user a clue to guess
# need to use conditions to guide e.g if random no.%2...
# if user guesses wrong another clue, score reduces

import random
print("Hey, welcome\nThis game allows you guess between the numbers 1 - 10\nTry guess right on your first try!\nYou can only guess twice\nGuess wrong and get your score cut in half\n...GOOD LUCK!\n")

no = random.randint(1, 10)
print(no)

if no % 2 == 0:
    print("\nFirst Hint: Number is even")
else:
    print("**First Hint: Number is odd")
    
User_Guess = int(input("Guess the number: "))

if User_Guess == no:
    print("You guessed right on your first try!\nScore: 100%")
elif User_Guess != no:
    print("\nWrong!\nScore: 50%\nTry again")
    
    if no >= 6:
        print("\n**Second Hint: Number is greater than 5")
    elif no <= 5:
        print("\nSecond Hint: Number is less than 6")
    user_guess = int(input("Guess the number: "))
    if user_guess == no:
        print("Correct!\nScore: 50%")
    else:
        print("Wrong!\n The number is:", no, "\nScore: 0%")