# Allow user to roll dice
# use choice to pick a number
# allow user to roll again till he wants to stop

import random

print("\nWelcome gamer\nLet's roll the dice!")
die = [1, 2, 3, 4, 5, 6]
roll_dice = int(input("Roll the dice? \nIf yes type '1', If no type '2' :  "))

if roll_dice != 1:
        print("Thank you for playing!")
print("You rolled:" , random.choice(die))

roll_again = int(input("Would you like to roll again? \nIf yes type '1', If no type '2' :  "))
if roll_again != 1:
        print("Thank you for playing!")
while roll_again == 1:
    print("You rolled:" , random.choice(die))
    roll_again = int(input("Would you like to roll again? \nIf yes type '1', If no type '2' :  "))  
    if roll_again != 1:
        print("Thank you for playing!")
        break
