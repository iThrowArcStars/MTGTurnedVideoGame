#roll.py
#This file contains a die rolling program

import random

def user_input_dice_quantity():
    while True:
        try:
            user_input = int(input("How many dice are rolled?: "))
        except (ValueError, TypeError):
            print("Invalid input, try again.")
            continue 
        break
    return user_input

def user_input_d_num():
    while True:
        try:
            user_input = int(input("How many sides does each die have?: "))
        except (ValueError, TypeError):
            print("Invalid response, try again.")
            continue
        break
    return user_input
    
def roll_dice(quantity, sides):
    total = 0
    for i in range(quantity):
        total += random.randint(1, sides)
    return total
    
def roll():
    quantity = user_input_dice_quantity()
    sides = user_input_d_num()
    print(roll_dice(quantity, sides))
    
if __name__ == "__main__":
    roll()