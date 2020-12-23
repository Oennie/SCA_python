# Allow user to roll dice
# use choice to pick a number
# allow user to roll again 

import random

print("\nWelcome gamer\nLet's roll the dice!")

roll_dice = str(input("Roll the dice? :  "))
die = [1, 2, 3, 4, 5, 6]
print(random.choice(die))

roll_again = str(input("Would you like to roll again? \nIf yes type 'continue', If no type 'stop' :  "))
if roll_again == "stop":
    print("Thank you playing!")
else:
    die = [1, 2, 3, 4, 5, 6]
    print(random.choice(die))
