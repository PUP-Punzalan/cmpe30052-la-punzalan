# Packages - import all the necessary packages
from tkinter import *
from tkinter import messagebox
import sys as program

# Creating a main window for the program
root = Tk()
root.geometry("600x300")
root.configure(bg="grey12")

# Lists
AddressBookList = [] # For storing all datas
searchChoices = [
    "First name",
    "Last name",
    "Address",
    "Contact number"
] # For sorting listbox

# String variables
firstName = StringVar()
lastName = StringVar()
address = StringVar()
contactNumber = StringVar()

# Variables
Count = 0 # For counting entries

# Colours used in the program
grey = "grey12"
white = "white"
lightGrey = "grey20"
lighestGrey = "grey80"
red = "red3"

# Add contact
def addContact():
    print("Added\n")
    global AddressBookList, Count
    if Count < 50: # Adding condition so that there is only 50 entries can be added
        if firstName.get() and lastName.get() and address.get() and contactNumber.get():
            AddressBookList.append([firstName.get(), lastName.get(), address.get(), contactNumber.get()])
            messagebox.showinfo("Address Book Manager", "Successfully added contact.")
            Count = Count + 1
            print(f"{Count} total contacts\n")
        else:
            messagebox.showerror("Warning", "Please input something in the following entries. Type N/A if you do not have the following information.")
    else:
        messagebox.showerror("Warning: Limit exceeded", "You have reached the maximum capacity of contacts.")
        print("Max!\n")
    updateListbox()
    resetEntries()

# Edit contact
def editContact():
    print("Edited\n")
    if listBox.curselection(): # Updating the selected contact with the new information in the entries
        edit = messagebox.askyesno("Address Book Manager", "Are you sure you want to edit?")
        if edit:
            AddressBookList[int(listBox.curselection()[0])][0] = firstName.get()
            AddressBookList[int(listBox.curselection()[0])][1] = lastName.get()
            AddressBookList[int(listBox.curselection()[0])][2] = address.get()
            AddressBookList[int(listBox.curselection()[0])][3] = contactNumber.get()
            messagebox.showinfo("Address Book Manager", "Successfully edited contact.")
            resetEntries()
    else:
        messagebox.showerror("Warning", "Please select an item in the list before clicking the Edit button")
    updateListbox()

# Delete contact
def deleteContact():
    print("Deleted\n")
    if listBox.curselection(): # Deleting the selected contact
        delete = messagebox.askyesno("Address Book Manager", "Are you sure you want to delete?")
        if delete:
            del AddressBookList[int(listBox.curselection()[0])]
    else:
        messagebox.showerror("Warning", "Please select an item in the list before clicking the Delete button")
    updateListbox()

# View contact
def viewContact():
    print("Viewed\n")
    if listBox.curselection(): # Viewing the selected contact in their respective entries
        firstName.set(AddressBookList[int(listBox.curselection()[0])][0])
        lastName.set(AddressBookList[int(listBox.curselection()[0])][1])
        address.set(AddressBookList[int(listBox.curselection()[0])][2])
        contactNumber.set(AddressBookList[int(listBox.curselection()[0])][3])
    else:
        messagebox.showerror("Warning", "Please select an item in the list before clicking the View button")

# Update listbox
def updateListbox(): # For updating the listbox every entry that is being added, deleted, or edited
    print("Updated\n")
    listBox.delete(0, END)
    for fname, lname, address, cnumber in AddressBookList:
        listBox.insert(END, fname)

# Update and sort listbox
def updateListboxSearch(choice):
    print("Updated Search\n")
    listBox.delete(0, END)
    for fname, lname, address, cnumber in AddressBookList: # For updating and sorting the listbox whatever the user choose
        if choice == "First name":
            listBox.insert(END, fname)
        elif choice == "Last name":
            listBox.insert(END, lname)
        elif choice == "Address":
            listBox.insert(END, address)
        elif choice == "Contact number":
            listBox.insert(END, cnumber)

# Reset entries
def resetEntries(): # For reseting or deleting all strings in every entries
    print("Reset\n")
    reset = messagebox.askyesno("Address Book Manager", "Are you sure you want to reset entries?")
    if reset:
        firstName.set("")
        lastName.set("")
        address.set("")
        contactNumber.set("")

# Exit Program
def exitProgram(): # For exiting the program
    print("Exit")
    exit = messagebox.askyesno("Exit application", "Are you sure you want to exit?")
    if exit:
        program.exit()

# Add N/A
# For adding N/A if the user does not have or want to input the information
def firstNameNA():
    firstName.set("N/A")
def lastNameNA():
    lastName.set("N/A")
def addressNA():
    address.set("N/A")
def contactNumberNA():
    contactNumber.set("N/A")

# Titles
Label(root, text="     Address Book Manager     ", font=("Helvetica", 18, "bold"), fg=white, bg=lightGrey).pack(padx=10, pady=10)
Label(root, text="Enter contact details", font=("Helvetica", 12, "bold"), fg=white, bg=grey).place(x=25, y=50)

# Labels and Entries
xLables = 50
yLables = 85
xEntries = 160
yEntries = 85

Label(root, text="First name", font=("Helvetica", 10), fg=white, bg=grey).place(x=xLables, y=yLables)
Entry(root, textvariable= firstName, font=("Helvertica", 10), fg=white, bg=lightGrey, bd=0).place(x=xEntries, y=yEntries)
Label(root, text="Last name", font=("Helvetica", 10), fg=white, bg=grey).place(x=xLables, y=yLables + 25)
Entry(root, textvariable= lastName, font=("Helvertica", 10), fg=white, bg=lightGrey, bd=0).place(x=xEntries, y=yEntries + 25)
Label(root, text="Address", font=("Helvetica", 10), fg=white, bg=grey).place(x=xLables, y=yLables + 50)
Entry(root, textvariable= address, font=("Helvertica", 10), fg=white, bg=lightGrey, bd=0).place(x=xEntries, y=yEntries + 50)
Label(root, text="Contact number", font=("Helvetica", 10), fg=white, bg=grey).place(x=xLables, y=yLables + 75)
Entry(root, textvariable= contactNumber, font=("Helvertica", 10), fg=white, bg=lightGrey, bd=0).place(x=xEntries, y=yEntries + 75)

# Buttons
xButtons = 25
yButtons = 200

# Function Buttons
Button(root, text="        ADD        ", command=addContact,
font=("Helvetica", 10, "bold"), bg=lighestGrey, bd=0).place(x=xButtons, y=yButtons)
Button(root, text="        EDIT        ", command=editContact,
font=("Helvetica", 10, "bold"), bg=lighestGrey, bd=0).place(x=xButtons + 110, y=yButtons)
Button(root, text="     DELETE      ", command=deleteContact,
font=("Helvetica", 10, "bold"), bg=lighestGrey, bd=0).place(x=xButtons, y=yButtons + 35)
Button(root, text="       VIEW        ", command=viewContact,
font=("Helvetica", 10, "bold"), bg=lighestGrey, bd=0).place(x=xButtons + 111, y=yButtons + 35)
Button(root, text="     RESET     ", command=resetEntries,
font=("Helvetica", 10, "bold"), bg=lighestGrey, bd=0).place(x=xButtons + 230, y=yButtons)
Button(root, text="       EXIT       ", command=exitProgram,
font=("Helvetica", 10, "bold"), bg=red, fg=white, bd=0).place(x=xButtons + 230, y=yButtons + 35)

# N/A Buttons
Button(root, text="N/A", command=firstNameNA,
font=("Helvetica", 7, "bold"), bg=lighestGrey, bd=0).place(x=xEntries + 150, y=yEntries)
Button(root, text="N/A", command=lastNameNA,
font=("Helvetica", 7, "bold"), bg=lighestGrey, bd=0).place(x=xEntries + 150, y=yEntries + 25)
Button(root, text="N/A", command=addressNA,
font=("Helvetica", 7, "bold"), bg=lighestGrey, bd=0).place(x=xEntries + 150, y=yEntries + 50)
Button(root, text="N/A", command=contactNumberNA,
font=("Helvetica", 7, "bold"), bg=lighestGrey, bd=0).place(x=xEntries + 150, y=yEntries + 75)

# Side listbox
searchTitle = Label(root, text="Search by:", font=("Helvetica", 12, "bold"), fg=white, bg=grey)
searchTitle.place(x=365, y=54)

clicked = StringVar()
clicked.set(searchChoices[0])

list = OptionMenu(root, clicked, *searchChoices, command=updateListboxSearch)
list.config(bd=0)
list.place(x=460, y=53)

# Listbox and scrollbar
frameRoot = Frame(root)
scrollBar = Scrollbar(frameRoot, orient=VERTICAL)
listBox = Listbox(frameRoot, yscrollcommand=scrollBar.set, width=35, height=10, bd=0, bg=grey, fg=white)
scrollBar.config(command=listBox.yview)

frameRoot.pack(side=RIGHT)
scrollBar.pack(side=RIGHT, fill=Y)
listBox.pack(side=LEFT, fill=BOTH, expand=1)

root.mainloop()