import random
random.seed(20)

class Dice:
    # A generic Dice
    __nr_sides = 0
    __current = 0
    
    def __init__(self,nr_sides, current):
        self.__nr_sides = nr_sides
        self.__current = current
        
    def roll(self):
        self.__current = random.randint(1,self.__nr_sides)
        
    def __str__(self):
        return str(self.__current)
    

my_dice = Dice(10,5)
my_dice.roll()
print(my_dice)