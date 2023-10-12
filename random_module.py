import random                                #import module
class Dice:                                  # dice class
    def roll(self):                          # Roll function
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second


dice = Dice()                                # create object "dice" for execut the
print(dice.roll())