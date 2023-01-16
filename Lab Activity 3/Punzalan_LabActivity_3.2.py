"""
Title: Animal
Submitted by: Amado Niño Rei Punzalan
Course & Section: BSCOE 2-1
"""

# Main class that stores all attributes
class ANIMAL:
    # Main constructor
    def __init__(self, name):
        self.name = name
        print("----------------------------\n  An animal has been born\n----------------------------")
    
    # Methods
    def eat(self):
        print("Munch munch!")
    
    def makeNoise(self):
        print(f"Grrr says {self.name}.\n")

class CAT(ANIMAL):
    # Sub constructor that is connected to the main constructor
    def __init__(self, name):
        super().__init__(name)
        print("A cat has been born.")
    
    # Sub method
    def makeNoise(self):
        print(f"Meow says {self.name}.\n")
    
class DOG(ANIMAL):
    # Sub constructor that is connected to the main constructor
    def __init__(self, name):
        super().__init__(name)
        print("A dog has been born.")

    # Sub method
    def makeNoise(self):
        print(f"Bark says {self.name}.\n")
    
# Objects
# Cats
cat1 = CAT("Pusa")
cat1.eat()
cat1.makeNoise()

# Dogs
dog1 = DOG("Unang Aso")
dog1.eat()
dog1.makeNoise()

dog2 = DOG("Pangalawang Aso")
dog2.eat()
dog2.makeNoise()

# Animals
animal1 = ANIMAL("Hayop")
animal1.eat()
animal1.makeNoise()