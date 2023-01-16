# Importing packages
from tkinter import *
from tkinter import messagebox
import sys as program

# Cash register class
class CASH_REGISTER:
    def __init__(self, cash_on_hand = 500):
        if cash_on_hand >= 0:
            self.__cash_on_hand = cash_on_hand
        else: self.__cash_on_hand = 500

    def currentBalance(self):
        return self.__cash_on_hand
        
    def acceptAmount(self, amount_in):
        self.__cash_on_hand += amount_in

# Dispenser class
class DISPENSER:
    def __init__(self, set_no_of_items = 50, set_cost = 50):
        if set_no_of_items >= 0 and set_cost >= 0:
            self.__set_no_of_items = set_no_of_items
            self.__set_cost = set_cost
        else:
            self.__set_no_of_items = 50
            self.__set_cost = 50
        
    def getCount(self):
        return self.__set_no_of_items

    def getProductCost(self):
        return self.__set_cost
    
    def makeSale(self):
        self.__set_no_of_items -= 1

# Color variables
grey = "grey12"
white = "white"
lightGrey = "grey20"
lighestGrey = "grey80"
red = "#f70000"
green = "#028752"
orange = "#f25a1d"

# Initializing main window
def main_window():
    global gui
    gui = Tk()
    gui.title("Candy Machine")
    gui.geometry("450x500")
    gui.configure(bg=grey)
main_window()

# Main values, variables, and objects
def main_values():
    global total_spent, total_cash, user_payment, total
    total_spent = StringVar()
    total_cash = StringVar()
    user_payment = StringVar()
    total = 0

    global cash_register_var, candy_dispenser, chips_dispenser, gum_dispenser, cookies_dispenser
    cash_register_var = CASH_REGISTER()
    candy_dispenser = DISPENSER()
    chips_dispenser = DISPENSER()
    gum_dispenser = DISPENSER()
    cookies_dispenser = DISPENSER()
main_values()

# Sell product function - will run if the user buys an item
def sellProduct(dispenser, cash_register):
    global total_spent, total
    while True:
        try:
            product_cost = dispenser.getProductCost()
            product_count = dispenser.getCount()
            if product_count:
                user_amount = int(user_payment.get())
                user_change = user_amount - product_cost
                user_payment.set("")

                if user_change >= 0:
                    cash_register.acceptAmount(product_cost)
                    dispenser.makeSale()
                    messagebox.showinfo("Candy Machine", f"Thank you for buying! Your change is {user_change} cents")
                    
                    total += product_cost
                    total_spent.set(f"{total} cents")
                    total_cash.set(f"{cash_register_var.currentBalance()} cents")
                    return
                else: 
                    messagebox.showwarning("Candy Machine", f"Insufficient amount. You need {product_cost-user_amount} cents more.")
                    return
            else: 
                messagebox.showwarning("Candy Machine", "The product is sold out.")
                return
        except ValueError:
            messagebox.showwarning("Candy Machine", "Please enter a valid amount.")
            return

# Candy function - will run if the user pressed the candy button
def candy():
    print("Candy")
    popup = Toplevel(gui)
    popup.title("Buy candy")
    popup.geometry("300x250")
    popup.configure(bg=grey)

    Label(popup, text=(f"Candy costs {candy_dispenser.getProductCost()} cents"),
    font=("Helvetica", 14, "bold italic"), fg=red, bg=grey).pack(pady=(20, 10))
    Label(popup, text="Enter amount", font=("Helvetica", 12, "bold"),
    fg=white, bg=grey).pack(pady=(0, 10))
    Entry(popup, textvariable=user_payment, font=("Helvetica", 14, "bold"),
    width=20, fg=green, bg=lightGrey, bd=0).pack(pady=(0, 20))
    Button(popup, text="Proceed", command=lambda: sellProduct(candy_dispenser, cash_register_var),
    fg=white, font=("Helvetica", 12, "bold"), bg=green, bd=0, width=10).pack(pady=(0, 20))

# Chips function - will run if the user pressed the chips button
def chips():
    print("Chips")
    popup = Toplevel(gui)
    popup.title("Buy chip")
    popup.geometry("300x250")
    popup.configure(bg=grey)

    Label(popup, text=(f"Chip costs {chips_dispenser.getProductCost()} cents"),
    font=("Helvetica", 14, "bold italic"), fg=red, bg=grey).pack(pady=(20, 10))
    Label(popup, text="Enter amount", font=("Helvetica", 12, "bold"),
    fg=white, bg=grey).pack(pady=(0, 10))
    Entry(popup, textvariable=user_payment, font=("Helvetica", 14, "bold"),
    width=20, fg=green, bg=lightGrey, bd=0).pack(pady=(0, 20))
    Button(popup, text="Proceed", command=lambda: sellProduct(chips_dispenser, cash_register_var),
    fg=white, font=("Helvetica", 12, "bold"), bg=green, bd=0, width=10).pack(pady=(0, 20))

# Gum function - will run if the user pressed the gum button
def gum():
    print("Gum")
    popup = Toplevel(gui)
    popup.title("Buy gum")
    popup.geometry("300x250")
    popup.configure(bg=grey)

    Label(popup, text=(f"Gum costs {gum_dispenser.getProductCost()} cents"),
    font=("Helvetica", 14, "bold italic"), fg=red, bg=grey).pack(pady=(20, 10))
    Label(popup, text="Enter amount", font=("Helvetica", 12, "bold"),
    fg=white, bg=grey).pack(pady=(0, 10))
    Entry(popup, textvariable=user_payment, font=("Helvetica", 14, "bold"),
    width=20, fg=green, bg=lightGrey, bd=0).pack(pady=(0, 20))
    Button(popup, text="Proceed", command=lambda: sellProduct(gum_dispenser, cash_register_var),
    fg=white, font=("Helvetica", 12, "bold"), bg=green, bd=0, width=10).pack(pady=(0, 20))

# Cookies function - will run if the user pressed the cookie button
def cookies():
    print("Cookies")
    popup = Toplevel(gui)
    popup.title("Buy cookie")
    popup.geometry("300x250")
    popup.configure(bg=grey)

    Label(popup, text=(f"Cookie costs {cookies_dispenser.getProductCost()} cents"),
    font=("Helvetica", 14, "bold italic"), fg=red, bg=grey).pack(pady=(20, 10))
    Label(popup, text="Enter amount", font=("Helvetica", 12, "bold"),
    fg=white, bg=grey).pack(pady=(0, 10))
    Entry(popup, textvariable=user_payment, font=("Helvetica", 14, "bold"),
    width=20, fg=green, bg=lightGrey, bd=0).pack(pady=(0, 20))
    Button(popup, text="Proceed", command=lambda: sellProduct(cookies_dispenser, cash_register_var),
    fg=white, font=("Helvetica", 12, "bold"), bg=green, bd=0, width=10).pack(pady=(0, 20))

# View function - will run if the user pressed the view balance button
def view():
    print("View")
    total_spent.set(f"{total} cents")
    total_cash.set(f"{cash_register_var.currentBalance()} cents")

    popup = Toplevel(gui)
    popup.title("Balance")
    popup.geometry("300x300")
    popup.configure(bg=grey)

    Label(popup, text="Total money spent:",
    font=("Helvetica", 12, "bold"), fg=white, bg=grey).p    ack(pady=(20, 10))
    Label(popup, textvariable=total_spent,
    font=("Helvetica", 16, "bold italic"), fg=green, bg=grey).pack(pady=(0, 10))
    Label(popup, text="Total cashier amount:",
    font=("Helvetica", 12, "bold"), fg=white, bg=grey).pack(pady=(0, 10))
    Label(popup, textvariable=total_cash,
    font=("Helvetica", 16, "bold italic"), fg=green, bg=grey).pack(pady=(0, 10))

# Exit function - will run if the user pressed the exit program button
def exit():
    print("Exit")
    exit = messagebox.askyesno("Exit application", "Are you sure you want to exit?")
    if exit:
        program.exit()

# Initializing labels and button to the main window
def labels_and_buttons():
    button_height = 1
    button_width = 25

    Label(gui, text="Candy Machine", font=("Helvetica", 18, "bold"),
    fg=white, bg=grey).pack(pady=(20, 10))
    Label(gui, text="To make a selection, click on the product button below.", font=("Helvetica", 11, "italic"),
    fg=white, bg=grey).pack(pady=(0, 20))

    Button(gui, text="Candy", command=candy, font=("Helvetica", 12, "bold"), bg=lighestGrey, bd=0,
    height=button_height, width=button_width).pack(pady=(0, 15))
    Button(gui, text="Chips", command=chips, font=("Helvetica", 12, "bold"), bg=lighestGrey, bd=0,
    height=button_height, width=button_width).pack(pady=(0, 15))
    Button(gui, text="Gum", command=gum, font=("Helvetica", 12, "bold"), bg=lighestGrey, bd=0,
    height=button_height, width=button_width).pack(pady=(0, 15))
    Button(gui, text="Cookies", command=cookies, font=("Helvetica", 12, "bold"), bg=lighestGrey, bd=0,
    height=button_height, width=button_width).pack(pady=(0, 15))
    Button(gui, text="View balance", command=view, font=("Helvetica", 12, "bold"), bg=green, bd=0, fg=white,
    height=button_height, width=button_width).pack(pady=(0, 15))
    Button(gui, text="Exit program", command=exit, font=("Helvetica", 12, "bold"), bg=red, bd=0, fg=white,
    height=button_height, width=button_width).pack(pady=(0, 15))
labels_and_buttons()

# Generating the main window
gui.mainloop()

