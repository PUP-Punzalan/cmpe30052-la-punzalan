# Imported packages
import sys

# Node class
class NODE:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# Linked list class
class LINKED_LIST:
    def __init__(self):
        self.head = None

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
|   [ 0 ] Quit program                                        |
|                                                             |
---------------------------------------------------------------

Enter your choice: """))
                
                if user_option == 1: # create list
                    number_of_elements = int(input("Enter number of nodes of the list: "))

                    for i in range(number_of_elements):
                        self.createList(int(input(f"Enter element {i+1}: ")))

                    self.displayElement()

                elif user_option == 2: # add at beginning
                    if self.head is None:
                        print("[ Warning ] Linked list is empty. Please create a list.")
                        self.mainProgram()
                        return

                    added_head_element = int(input("Enter element to be added at the beginnning: "))
                    self.insertAtBeginning(added_head_element)
                    self.displayElement()

                elif user_option == 3: # add element with position
                    if self.head is None:
                        print("[ Warning ] Linked list is empty. Please create a list.")
                        self.mainProgram()
                        return

                    added_element = int(input("Enter element to be added: "))
                    added_position = int(input(f"Enter what index you want to add the element (0-{self.countElement()}): "))
                    self.insertAtN(added_position, added_element)
                    self.displayElement()

                elif user_option == 4: # delete element
                    if self.head is None:
                        print("[ Warning ] Linked list is empty. Please create a list.")
                        self.mainProgram()
                        return
                        
                    deleted_element = int(input("Enter element to be deleted: "))
                    self.removeElement(deleted_element)
                    self.displayElement()

                elif user_option == 5: # display list
                    if self.head is None:
                        print("[ Warning ] Linked list is empty. Please create a list.")
                        self.mainProgram()
                        return
                        
                    self.displayElement()

                elif user_option == 6: # count element
                    if self.head is None:
                        print("[ Warning ] Linked list is empty. Please create a list.")
                        self.mainProgram()
                        return
                        
                    print(f"[ Info ] The number of elements in the list is {self.countElement()}.")
                    self.displayElement()

                elif user_option == 7: # reverse list
                    if self.head is None:
                        print("[ Warning ] Linked list is empty. Please create a list.")
                        self.mainProgram()
                        return
                        
                    self.reverseList()
                    self.displayElement()

                elif user_option == 8: # search element
                    if self.head is None:
                        print("[ Warning ] Linked list is empty. Please create a list.")
                        self.mainProgram()
                        return
                        
                    self.searchElement(int(input(f"Enter element to be searched: ")))
                    self.displayElement()

                elif user_option == 0: # quit program
                    sys.exit("[ Info ] Thank you for using the program!")

                elif user_option > 8 or user_option < 1: # entered invalid element
                    raise ValueError() # recognize as error to proceed in except

            except ValueError: # if theres an error
                print("[ Error ] Invalid element! Please enter an integer.")

    def createList(self, u_value): # to create a list
        if self.head is None:
            self.head = NODE(u_value)
            return
        
        iterate = self.head
        while iterate.next:
            iterate = iterate.next
        iterate.next = NODE(u_value, None)

    def insertAtBeginning(self, u_value): # to add an element at the beginning
        node = NODE(u_value, self.head)
        self.head = node

    def insertAtN(self, index, u_value): # to add an element at specific position
        if index < 0 or index > self.countElement():
            print("[ Error ] Invalid index.")

        if index == 0:
            self.insertAtBeginning(u_value)
            return

        count = 0
        iterate = self.head
        while iterate:
            if count == index - 1:
                node = NODE(u_value, iterate.next)
                iterate.next = node
                break

            iterate = iterate.next
            count += 1

    def removeElement(self, u_value): # to remove an element
        if self.head is None:
            print("[ Warning ] Linked list is empty. Please create a list.")
            return
        
        iterate = self.head
        position = 0

        if self.head.value == u_value:
            self.head = self.head.next
            print(f"[ Info ] Element {u_value} has been deleted at position {position + 1}.")
            return

        while iterate.next:
            if iterate.next.value == u_value:
                iterate.next = iterate.next.next
                print(f"[ Info ] Element {u_value} has been deleted at position {position + 2}.")
                return
            
            position += 1
            iterate = iterate.next
            
        print("[ Warning ] Element not found!")

    def displayElement(self): # to diplay the element/s  
        iterate = self.head
        llstr = ''
        while iterate:
            llstr += str(iterate.value) + ' --> '
            iterate = iterate.next
        print(f"List: {llstr}")

    def countElement(self): # to count the element/s
        count = 0
        iterate = self.head
        while iterate:
            count+=1
            iterate = iterate.next

        return count
    
    def reverseList(self): # to reverse the order of the elements
        if self.head is None:
            print("[ Warning ] Linked list is empty. Please create a list.")
            return

        previous = None
        current = self.head
        following = current.next

        while current:
            current.next = previous
            previous = current
            current = following

            if following:
                following = following.next
        
        self.head = previous

    def searchElement(self, u_value): # to search for an element
        iterate = self.head
        position = 0

        while iterate:
            if iterate.value == u_value:
                print(f"[ Info ] Element {u_value} has been found at position {position + 1}.")
                return 
            
            position += 1
            iterate = iterate.next
        print(f"[ Warning ] Element {u_value} has not been found. Please try again.")

# Object
user_01 = LINKED_LIST()
user_01.mainProgram()