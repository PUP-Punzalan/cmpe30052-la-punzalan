# Imported packages
import sys

# Main list
user_list = []

# Main class
class LINKED_LIST:
    global user_list

    # Main program/method
    def mainProgram(self):
        while True:
            try:
                user_option = int(input("""
-------------------- LINKED LIST IN PYTHON --------------------
|   Programmed by: Amado Niño Rei Punzalan                    |
|   Course & Section: BSCOE 2-1                               |
|                                                             |
|   Main menu:                                                | 
|   [ 1 ] Create list                                         |
|   [ 2 ] Add at beginning                                    |
|   [ 3 ] Add at specific index                               |
|   [ 4 ] Delete element                                      |
|   [ 5 ] Display list                                        |
|   [ 6 ] Count element                                       |
|   [ 7 ] Reverse list                                        |
|   [ 8 ] Search element                                      |
|   [ 9 ] Clear list                                          |
|   [ 0 ] Quit program                                        |
|                                                             |
---------------------------------------------------------------

Enter your choice: """))
                
                if user_option == 1: # create list
                    self.createList()
                elif user_option == 2: # add at beginning
                    self.addBeginning()
                elif user_option == 3: # add element with position
                    self.addElement()
                elif user_option == 4: # delete element
                    self.deleteElement()
                elif user_option == 5: # display list
                    self.displayElement()
                elif user_option == 6: # count element
                    self.countElement()
                elif user_option == 7: # reverse list
                    self.reverseList()
                elif user_option == 8: # search element
                    self.searchElement()
                elif user_option == 9: # clear list
                    self.clearList()
                elif user_option == 0: # quit program
                    self.quitProgram()
                elif user_option > 9 or user_option < 1: # entered invalid element
                    raise ValueError() # recognize as error to proceed in except
                print(f"""
---------------------------------------------------------------
    List: {' -> '.join(str(i) for i in user_list)}
---------------------------------------------------------------""")

            except ValueError: # if theres an error
                print("[ Error ] Invalid element! Please enter an integer.")
                print(f"""
---------------------------------------------------------------
    List: {' -> '.join(str(i) for i in user_list)}
---------------------------------------------------------------""")

    def createList(self): # to create a list or append new sets of elements
        element_num = int(input("Enter how many node in the list: "))
        
        for i in range(element_num):
            user_list.append(int(input(f"Element {i+1}: ")))
    
    def addBeginning(self): # to add an element at the beginning
        added_beginning = int(input("Enter element to be added at the beginning: "))
        user_list.insert(0, added_beginning)
        print(f"\n[ Info ] Element {added_beginning} has been added at position {user_list.index(added_beginning) + 1}.")
    
    def addElement(self): # to add an element at the specific location
        added_element = int(input("Enter element to be added: "))
        element_pos = int(input(f"Enter what position you want to add the element (1-{len(user_list) + 1}): "))
        if element_pos <= len(user_list) + 1:
            user_list.insert(element_pos - 1, added_element)
            print(f"\n[ Info ] Element {added_element} has been added at position {element_pos}.")
        else:
            print(f"[ Error ] Invalid amount! Please enter an index ranging from 1 to {len(user_list) + 1}")
            self.addElement()
    
    def deleteElement(self): # to delete an element in the list and update the positions of the remaining elements
        deleted_element = int(input("Enter element to be deleted: "))

        if deleted_element in user_list:
            print(f"\n[ Info ] Element {deleted_element} has been deleted at position {user_list.index(deleted_element) + 1}.")
            user_list.remove(deleted_element)
        else: print("\n[ Error ] Element not found. Please try again.")
    
    def displayElement(self): # to display the elements
        print(f"""
---------------------------------------------------------------
    List: {' -> '.join(str(i) for i in user_list)}
---------------------------------------------------------------""")
    
    def countElement(self): # to count the elements in the list
        if len(user_list) > 0:
            print(f"[ Info ] The number of elements in the list is {len(user_list)}.")
        else: print("[ Error ] No list found! Please create a list.")
    
    def reverseList(self): # to reverse the order of the elements in the list
        if len(user_list) > 1:
            print(f"""
---------------------------------------------------------------
    List: {' -> '.join(str(i) for i in user_list)}
---------------------------------------------------------------""")
            user_list.reverse()
        else: print("[ Error ] No list or there is only one element! Please create a list or add more element.")
        
    def searchElement(self): # to search an element
        searched_element = int(input("Enter element to be searched: "))

        if searched_element in user_list:
            print(f"[ Info ] Element {searched_element} has been found at position {user_list.index(searched_element) + 1}.")
        else: print("[ Error ] Element not found. Please try again.")
    
    def clearList(self): # to clear the list
        user_list.clear()

    def quitProgram(self): # to quit the program
        sys.exit("[ Info ] Thank you for using the program!")
    
# Objects
user_01 = LINKED_LIST()
user_01.mainProgram()