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

# Main program class     
class MAIN_PROGRAM:
    # Shows selection and import selection to a variable
    def showSelection(self):
        global food
        food = int(input("""
~ Welcome to Candy's Candy Shop ~
To select an item enter:
[ 1 ] for Candy
[ 2 ] for Chips
[ 3 ] for Gum
[ 4 ] for Cookies
[ 0 ] to View balance
[ 9 ] to Exit program

Enter your choice here: """))

    # Runs when the user choose to buy something
    def sellProduct(self, dispenser, cash_register):
        while True:
            try: # tries to run the function/method
                product_cost = dispenser.getProductCost() # gets the cost of the specific product
                product_count = dispenser.getCount() # gets the count of the specific product
                
                if product_count: # runs if there is a product
                    print(f"Cost: {product_cost} cents")
                    user_amount = int(input("Enter amount: "))
                    user_change = user_amount - product_cost

                    if user_change >= 0: # runs if there is a sufficient amount entered
                        print(f"Your change is: {user_change}\n")
                        cash_register.acceptAmount(product_cost)
                        dispenser.makeSale()
                        return
                    else: # runs if there is insufficient amount entered
                        print(f"You have insufficient amount. You need {product_cost - user_amount} cents more\n")
                else: # runs if there is no product
                    print("The product is sold out.")
                    return
            except ValueError: # run if the entered amount is not an integer
                print("Enter valid amount.")

    # Main program method that runs any necessary method needed
    def mainProgram(self):
        # Generating objects for every products
        cash_register = CASH_REGISTER()
        candy = DISPENSER()
        chips = DISPENSER()
        gum = DISPENSER()
        cookies = DISPENSER()

        while True:
            self.showSelection()

            if food == 1:
                self.sellProduct(candy, cash_register)
            elif food == 2:
                self.sellProduct(chips, cash_register)
            elif food == 3:
                self.sellProduct(gum, cash_register)
            elif food == 4:
                self.sellProduct(cookies, cash_register)
            elif food == 0:
                print(f"Current balance: {cash_register.currentBalance()}")
            elif food == 9:
                break

# Running the program
program = MAIN_PROGRAM()
program.mainProgram()