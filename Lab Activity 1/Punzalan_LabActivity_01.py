'''
Program name: Address Book Manager
Description:
    This program can be used to save, edit, delete, view, and search your following information:
    first name, last name, address, and contact number.
'''

# Lists and variables
FirstName = [] # Storing first names
LastName = [] # Storing last names
Address = [] # Storing addresses
ContactNumber = [] # Storing contact numbers
EntryNumber = [] # Storing entries
Count = 0 # Counting entries

# Functions
# Add contact function is responsible for
# adding and saving contacts to their respective lists
def addContact():
    global Count
    print(""
        "\n----------------------------------------------------------------------\n"
        "Instructions:\n"
        "    - Input all necessary details\n"
        "    - Put N/A if you don't have anything to type\n"
        "----------------------------------------------------------------------")
    userFirstName = input("First name: ")
    userLastName = input("Last name: ")
    userAddress = input("Address: ")
    userContactNumber = input("Contact number: ")

    # Storing inputs in lists
    FirstName.append(userFirstName)
    LastName.append(userLastName)
    Address.append(userAddress)
    ContactNumber.append(userContactNumber)
    Count = Count + 1 # Adding 1 per contact to track the entries
    EntryNumber.append(Count)

# View contact function is for viewing all the contacts
def viewContact():
    for i in range(len(EntryNumber)):
        print(f""
            "----------------------------------------\n"
            f"       Contact information: {EntryNumber[i]}\n"
            "----------------------------------------\n"
            f"Entry number: {EntryNumber[i]}\n"
            f"First name: {FirstName[i]}\n"
            f"Last name: {LastName[i]}\n"
            f"Address: {Address[i]}\n"
            f"Contact number: {ContactNumber[i]}\n")

# Edit contact function is for editing specific entry within the lists
def editContact():
    while True:
        viewContact()
        entryNumber = int(input("What entry do you wish to edit? Enter entry number: "))
        if entryNumber <= len(EntryNumber):
            index = entryNumber - 1 # Subtracting 1 to get the list index
            
            print(f""
                "\n----------------------------------------\n"
                f"    Contact information: {EntryNumber[index]}\n"
                "----------------------------------------\n"
                f"Entry number: {EntryNumber[index]}\n"
                f"First name: {FirstName[index]}\n"
                f"Last name: {LastName[index]}\n"
                f"Address: {Address[index]}\n"
                f"Contact number: {ContactNumber[index]}\n"
                "------------------------------------------\n")

            infoToEdit = int(input(""
                "---------------------------\n"
                "What do you wish to edit?\n"
                "    [1] - First name\n"
                "    [2] - Last name\n"
                "    [3] - Address\n"
                "    [4] - Contact number\n"
                "---------------------------\n"
                "Choose from 1 to 4: "))
            
            # Adding conditions to track what the user choose,
            # then run the specified function
            if infoToEdit == 1:
                FirstName[index] = input("Input new first name: ")
            elif infoToEdit == 2:
                LastName[index] = input("Input new last name: ")
            elif infoToEdit == 3:
                Address[index] = input("Input new address: ")
            elif infoToEdit == 4:
                ContactNumber[index] = input("Input new contact number: ")
            else:
                print("Error! Enter number only from 1 to 4.")
                break
            
            # Printing the edited/updated entry
            print(f""
                "----------------------------------------\n"
                f"    Contact information: {EntryNumber[index]}\n"
                "----------------------------------------\n"
                f"Entry number: {EntryNumber[index]}\n"
                f"First name: {FirstName[index]}\n"
                f"Last name: {LastName[index]}\n"
                f"Address: {Address[index]}\n"
                f"Contact number: {ContactNumber[index]}\n"
                "------------------------------------------\n")
        else:
            print(f"Please enter value from 1 to {len(EntryNumber)}. Please try again.")
            break
        break

# Delete contact function is for deleting specific entry in the list
def deleteContact():
    global Count
    while True:
        viewContact()
        entryToDelete = int(input("What entry do you wish to delete? Enter entry number: "))
        if entryToDelete <= len(EntryNumber):
            index = entryToDelete - 1 # Subtracting 1 to get the list index

            # Using pop function to remove the specific index in the list
            FirstName.pop(index)
            LastName.pop(index)
            Address.pop(index)
            ContactNumber.pop(index)

            Count = Count - 1 # Subtracting 1 because we are deleting a contact/entry
            del EntryNumber[-1] # Deleting the last number in the list

            viewContact()
        else:
            print(f"There is no entry {entryToDelete} on the list. Please try again.")
            break
        break

# Search contact function is for searching a specific entry/contact in the list
def searchContact():
    while True:
        # Using lower function to convert all information to lowercase,
        # with that we can search no matter what cases we input,
        # as long as we input the right spelling
        lowerFirstName = [fname.lower() for fname in FirstName]
        lowerLastName = [lname.lower() for lname in LastName]
        lowerAddress = [address.lower() for address in Address]
        lowerContactNumber = [cnumber.lower() for cnumber in ContactNumber]

        searchByWhat = int(input(""
            "------------------------------------------\n"
            "What do you want to use to search entry?\n"
            "   [1] - By first name\n"
            "   [2] - By last name\n"
            "   [3] - By address\n"
            "   [4] - By contact number\n"
            "------------------------------------------\n"
            "Choose from 1 to 4: "))

        # Added condition to track what the user chooses,
        # then run the specific condition
        if searchByWhat == 1: # First name search
            searchWhat = input("Enter first name to search: ")
            lowerSearchWhat = searchWhat.lower()
            for i in range(len(lowerFirstName)):
                if lowerSearchWhat in lowerFirstName[i]:
                    print(f""
                        "----------------------------------------------------------------------\n"
                        f"Entry number: {EntryNumber[i]}\n"
                        f"First name: {FirstName[i]}\n"
                        f"Last name: {LastName[i]}\n"
                        f"Address: {Address[i]}\n"
                        f"Contact Number: {ContactNumber[i]}\n"
                        "----------------------------------------------------------------------\n")
            break
        elif searchByWhat == 2: # Last name search
            searchWhat = input("Enter last name to search: ")
            lowerSearchWhat = searchWhat.lower()
            for i in range(len(lowerLastName)):
                if lowerSearchWhat in lowerLastName[i]:
                    print(f""
                        "----------------------------------------------------------------------\n"
                        f"Entry number: {EntryNumber[i]}\n"
                        f"First name: {FirstName[i]}\n"
                        f"Last name: {LastName[i]}\n"
                        f"Address: {Address[i]}\n"
                        f"Contact Number: {ContactNumber[i]}\n"
                        "----------------------------------------------------------------------\n")
            break
        elif searchByWhat == 3: # Address search
            searchWhat = input("Enter address to search: ")
            lowerSearchWhat = searchWhat.lower()
            for i in range(len(lowerAddress)):
                if lowerSearchWhat in lowerAddress[i]:
                    print(f""
                        "----------------------------------------------------------------------\n"
                        f"Entry number: {EntryNumber[i]}\n"
                        f"First name: {FirstName[i]}\n"
                        f"Last name: {LastName[i]}\n"
                        f"Address: {Address[i]}\n"
                        f"Contact Number: {ContactNumber[i]}\n"
                        "----------------------------------------------------------------------\n")
            break
        elif searchByWhat == 4: # Contact number search
            searchWhat = input("Enter contact number to search: ")
            lowerSearchWhat = searchWhat.lower()
            for i in range(len(lowerContactNumber)):
                if lowerSearchWhat in lowerContactNumber[i]:
                    print(f""
                        "----------------------------------------------------------------------\n"
                        f"Entry number: {EntryNumber[i]}\n"
                        f"First name: {FirstName[i]}\n"
                        f"Last name: {LastName[i]}\n"
                        f"Address: {Address[i]}\n"
                        f"Contact Number: {ContactNumber[i]}\n"
                        "----------------------------------------------------------------------\n")
            break
        else:
            print("Please enter number from 1 to 4 only. Please try again.")
            break

# Main body function is for running the whole code
def AskWhatFunction():
    global Count
    while Count <= 50:
        whatFunction = input(""
            "----------------------------\n"
            "What would you like to do?\n"
            "    [1] - Add contact\n"
            "    [2] - Edit contact\n"
            "    [3] - Delete contact\n"
            "    [4] - View contact(s)\n"
            "    [5] - Search contact\n"
            "    [6] - Exit program\n"
            "----------------------------\n"
            "Choose from 1 to 6: ")

        # Added condition to track what the user want to do
        if whatFunction == "1":
            addContact()
        elif whatFunction == "2":
            editContact()
        elif whatFunction == "3":
            deleteContact()
        elif whatFunction == "4":
            viewContact()
        elif whatFunction == "5":
            searchContact()
        else:
            break

# Calling the main function to run the whole code
AskWhatFunction()