"""
Title: The Combinational Lock
Submitted by: Amado Niño Rei Punzalan
Course & Section: BSCOE 2-1
"""

# Packages imported
from random import randint

# Main class that stores all attributes and methods
class COMBO_LOCK:
    # Constructor
    def __init__(self, secret1, secret2, secret3):
        if secret1 < 0:
            self.secret1 = 0
        elif secret1 > 39:
            self.secret1 = 39
        else: self.secret1 = secret1

        if secret2 < 0:
            self.secret2 = 0
        elif secret2 > 39:
            self.secret2 = 39
        else: self.secret2 = secret2

        if secret3 < 0:
            self.secret3 = 0
        elif secret3 > 39:
            self.secret3 = 39
        else: self.secret3 = secret3

        self.current_number = 0
        self.status = 0
    
    # Reset method that resets the lock
    def reset(self):
        self.current_number = 0
        self.status = 0
        print("[ Info ] The lock has been reset.\n")
    
    # Turn left method, that move the tick to the left side
    def turnLeft(self, ticks): # negative/subtact
        if ticks <= 40:
            self.current_number -= ticks

            if self.current_number > 39:
                self.current_number -= 40
                print(f"[ Info ] You ticked {ticks} times to the left. You're current number is {self.current_number}.")
            elif self.current_number < 0:
                self.current_number += 40
                print(f"[ Info ] You ticked {ticks} times to the left. You're current number is {self.current_number}.")
            elif self.current_number > -1 and self.current_number < 40:
                print(f"[ Info ] You ticked {ticks} times to the left. You're current number is {self.current_number}.")

            if self.secret2 == self.current_number and self.status == 1:
                print("[ Info ] You have unlocked number 2 lock.\n")
                self.status = 2
            else: print("[ Info ] You did not unlocked any lock, please try again.\n")
        else: print("[ Warning ] Please enter number 1 to 40 only.\n")

    # Turn right method, that move the tick to the right side
    def turnRight(self, ticks): # positive/add
        if ticks <= 40:
            self.current_number += ticks

            if self.current_number > 39:
                self.current_number -= 40
                print(f"[ Info ] You ticked {ticks} times to the right. You're current number is {self.current_number}.")
            elif self.current_number < 0:
                self.current_number += 40
                print(f"[ Info ] You ticked {ticks} times to the right. You're current number is {self.current_number}.")
            elif self.current_number > -1 and self.current_number < 40:
                print(f"[ Info ] You ticked {ticks} times to the right. You're current number is {self.current_number}.")

            if self.secret1 == self.current_number and self.status == 0:
                print("[ Info ] You have unlocked number 1 lock.\n")
                self.status = 1
            elif self.secret3 == self.current_number and self.status == 2:
                print("[ Info ] You have unlocked number 3 lock.\n")
                self.status = 3
            else: print("[ Info ] You did not unlocked any lock, please try again.\n")
        else: print("[ Warning ] Please enter number 1 to 40 only.\n")

    # Open method that tries to open the lock, if the user got all the combination it will open,
    # and it will not open if the user did not get the combinations
    def open(self):
        if self.status < 3:
            print("[ Info ] Cannot open! Please unlock all the remaining locks first before opening.\n")
        else:
            print("[ Info ] Lock opened!\n")

# Object for password
password = COMBO_LOCK(1, 2, 24)

# Main program function, runs the whole program
def mainProgram():
    # while loop, to repeatedly ask the user
    while True:
        print("------------------------------\n        Combo Lock\n------------------------------")
        print("Choose a number to proceed:\n[ 1 ] Turn left\n[ 2 ] Turn right\n[ 3 ] Open lock\n[ 4 ] Reset lock\n[ 0 ] Exit program\n")
        choice = int(input("Enter number: "))

        # if-else statements, runs specified methods by the user choice
        if choice == 1:
            if password.status == 1:
                left_ticks = int(input("Enter amount of left ticks: "))
                password.turnLeft(left_ticks)
            else: 
                print(f"[ Warning ] Please turn right. You are still on number {password.status + 1} lock.\n")
                mainProgram()
        elif choice == 2:
            if password.status == 0 or password.status == 2:
                right_ticks = int(input("Enter amount of right ticks: "))
                password.turnRight(right_ticks)
            else: 
                print(f"[ Warning ] Please turn left. You are still on number {password.status + 1} lock.\n")
                mainProgram()
        elif choice == 3:
            password.open()
        elif choice == 4:
            password.reset()
        elif choice == 0:
            return
        else: 
            print("[ Warning ] Please enter a valid number.\n")
            mainProgram()

mainProgram()