import random
random.seed(20)

class Dice:
    def __init__(self, num_sides, dice_showing):
        self.num_sides = num_sides
        self.dice_showing = dice_showing
 
    def roll(self) ->None:        
        for nr in range( 1, self.num_sides):
            __random_num = random.randint(1,self.num_sides)
            self.dice_showing = __random_num
 
    def __str__(self) -> str:
        return '{}'.format(self.dice_showing)
    

my_dice = Dice(10,5)
my_dice.roll()
print(my_dice)