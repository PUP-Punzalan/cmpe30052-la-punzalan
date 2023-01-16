"""
Title: The Stock Class
Submitted by: Amado Niño Rei Punzalan
Course & Section: BSCOE 2-1
Additional info: I added some extra methods to increase what the program can do.
"""

# Main class that stores all attributes and methods
class STOCK:
    # Constructor
    def __init__(self, symbol, name, prev_closing_price, current_price):
        self.__symbol = str(symbol)
        self.__name = str(name)
        self.__prev_closing_price = float(prev_closing_price)
        self.__current_price = float(current_price)

    # Get methods
    def getName(self):
        return self.__name

    def getSymbol(self):
        return self.__symbol

    def getPreviousClosingPrice(self):
        return self.__prev_closing_price

    def getCurrentPrice(self):
        return self.__current_price

    def getChangePercent(self):
        percent_change = round((self.__current_price - self.__prev_closing_price) / self.__prev_closing_price * 100, 2)
        return percent_change
    
    # Set methods
    def setName(self, name): # additional method
        self.__name = name
        return self.__name

    def setSymbol(self, symbol): # additional method
        self.__symbol = symbol
        return self.__symbol

    def setPreviousClosingPrice(self, prev_price):
        self.__prev_closing_price = prev_price
        return self.__prev_closing_price
    
    def setCurrentPrice(self, current_price):
        self.__current_price = current_price
        return self.__current_price

# Object
test_object = STOCK("INTC", "Intel Corporation", 20.5, 20.35)

# Print function
def printObjects():
    print("---------------------------------\n     Percent Change Solver\n---------------------------------")
    print(f"Your price change is: {test_object.getChangePercent()}%\n")

printObjects()