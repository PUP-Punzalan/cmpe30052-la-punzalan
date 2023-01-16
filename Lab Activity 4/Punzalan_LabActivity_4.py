# Imported packages
import sys

# Main class for sorting algorithm
class SORTING:
    # Selection sort algorithm
    def selectionSort(self, lst):
        for i in range(len(lst)-1): # to sort every element in the list
            current_min = i
            for j in range(i+1, len(lst)): # to compare the current element to other elements
                if sorting_mode == 1 or sorting_mode == 3: # ascending or alphabetical order
                    if lst[j] < lst[current_min]:
                        current_min = j
                elif sorting_mode == 2:
                    if lst[j] > lst[current_min]: # descending order
                        current_min = j
            
            if current_min != i: # to swap the numbers if they are not the same
                lst[i], lst[current_min] = lst[current_min], lst[i]

            print(f"Pass {i+1}: {lst}") # to print steps/passes

    # Bubble sort algorithm
    def bubbleSort(self, lst):
        for i in range(len(lst)-1): # to sort every element in the list
            for j in range(0, len(lst)-1): # to compare the current element to other element
                if sorting_mode == 1 or sorting_mode == 3: # ascending or alphabetical order
                    if lst[j] > lst[j+1]:
                        lst[j], lst[j+1] = lst[j+1], lst[j]
                elif sorting_mode == 2: # descending order
                    if lst[j] < lst[j+1]:
                        lst[j], lst[j+1] = lst[j+1], lst[j]
            
            print(f"Pass {i+1}: {lst}") # to print steps/passes

    # Insertion sort algorithm
    def insertionSort(self, lst):
        for i in range(1, len(lst)): # to sort every element in the list
            j = i
            # To swap if right number is higher than the left number
            while j > 0 and lst[j-1] > lst[j] and sorting_mode == 1 or sorting_mode == 3: # ascending or alphabetical order
                lst[j], lst[j-1] = lst[j-1], lst[j]
                j = j - 1
            while j > 0 and lst[j-1] < lst[j] and sorting_mode == 2: # descending order
                lst[j], lst[j-1] = lst[j-1], lst[j]
                j = j - 1

            print(f"Pass {i}: {lst}") # to print steps/passes

    # Merge sort algorithm
    def mergeSort(self, lst):
        if len(lst) > 1: # to check if list contains 2 or more element
            mid = len(lst) // 2 # divide list
            left = lst[:mid]
            right = lst[mid:]

            # To divide the divided list
            self.mergeSort(left)
            self.mergeSort(right)

            uno = dos = alas = 0

            while uno < len(left) and dos < len(right): 
                if sorting_mode == 1 or sorting_mode == 3: # ascending or alphabetical order
                    if left[uno] < right[dos]:
                        lst[alas] = left[uno]
                        uno += 1
                    else:
                        lst[alas] = right[dos]
                        dos += 1
                elif sorting_mode == 2: # descending order
                    if left[uno] > right[dos]:
                        lst[alas] = left[uno]
                        uno += 1
                    else:
                        lst[alas] = right[dos]
                        dos += 1
                alas += 1
            
            while uno < len(left):
                lst[alas] = left[uno]
                uno += 1
                alas += 1
            
            while dos < len(right):
                lst[alas] = right[dos]
                dos += 1
                alas += 1

            print(f"Pass {uno-1+1}: {left} and {right}") # to print steps/passes

# Global variables         
object = SORTING()
main_list = []

# Main program
def program():
    global sorting_mode, data_type, sort_mode, sort_type
    main_list.clear()
    try:
        while True:
            user_option = int(input("""
-------- SORTING ALGORITHM APPLICATION --------
|  Programmed by: Amado Niño Rei Punzalan     |
|  Course & Section: BSCOE 2-1                |
|                                             |
|  MAIN MENU:                                 |
|  [ 1 ] Selection sorting                    |
|  [ 2 ] Bubble sorting                       |
|  [ 3 ] Insertion sorting                    |
|  [ 4 ] Merge sorting                        |
-----------------------------------------------

Select an option: """))

            element_num = int(input("Number of elements on the list: "))
            element_type = int(input("""
------------ ELEMENT TYPE ------------
|  [ 1 ] Integers                    |
|  [ 2 ] Letters (Upper-case only)   |
--------------------------------------

Enter element type: """))

            sorting_mode = int(input("""
----------- SORTING MODE -----------
|  [ 1 ] Ascending                 |
|  [ 2 ] Descending                |
|  [ 3 ] Alphabetical              |
------------------------------------

Enter sorting mode: """))

            if element_type == 1: # if integer
                data_type = "INTEGER"
                for i in range(element_num):
                    main_list.append(int(input(f"Element {i+1}: ")))
            elif element_type == 2: # if letter
                data_type = "LETTER"
                for i in range(element_num):
                    user_input = input(f"Element {i+1}: ")
                    if user_input.isupper() == True:
                        main_list.append(user_input)
                    else:
                        print("[ Warning ] Upper-case letters only!")
                        
                        run_again = input("Do you want to run again? [Y/N] ").upper()
                        if run_again == "N":
                            sys.exit("\nThank you for using the program!\n")
                        elif run_again == "Y":
                            program()
                        else:
                            print("[ Warning ] Please enter a valid number.")
                            program()

            if user_option == 1:
                sort_type = "Selection"
            elif user_option == 2:
                sort_type = "Bubble"
            elif user_option == 3:
                sort_type = "Insertion"
            elif user_option == 4:
                sort_type = "Merge"
            
            if sorting_mode == 1:
                sort_mode = "Ascending"
            elif sorting_mode == 2:
                sort_mode = "Descending"
            elif sorting_mode == 3:
                sort_mode = "Alphabetical"

            print(f"Enter your {element_num} {data_type} (press Enter to end every element): ")
            print(f"""
-----------------------------
    List: {main_list}
    Type: {sort_type} sorting 
    Order: {sort_mode}
-----------------------------
""")

            if user_option == 1:
                object.selectionSort(main_list)
            elif user_option == 2:
                object.bubbleSort(main_list)
            elif user_option == 3:
                object.insertionSort(main_list)
            elif user_option == 4:
                object.mergeSort(main_list)
            
            print(f"""
-----------------------------
    Result: {main_list}
-----------------------------
""")
            main_list.clear()

            run_again = input("Do you want to run again? [Y/N] ").upper()
            if run_again == "N":
                sys.exit("\nThank you for using the program!\n")
            
    except ValueError:
        print(f"[ Warning ] Invalid character. Please enter {data_type} element.")
        program()

program()