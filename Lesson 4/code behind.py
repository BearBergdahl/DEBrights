import random

class Character:
    rpg = 'DnD'
    def __init__(self, name, player, character_class):
        self.name = name
        self.player = player
        self.character_class = character_class

    def roll_dice(self, sides):
        if (type(sides) == type(1)):
            roll_result = random.randint(1,sides)
            return f'{self.name} the {self.character_class} rolled a {roll_result}'
# Can be made into a static
    @staticmethod
    def static_roll_dice( sides):
        if (type(sides) == type(1)):
            roll_result = random.randint(1,sides)
            return roll_result

brynhilde = Character('Brynhilde', 'Björn', 'Valkyrie')
print(brynhilde.roll_dice(20))
print(Character.static_roll_dice(12))
