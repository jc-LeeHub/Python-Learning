from random import randint

class Die():

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    #返回1和骰子面数之间的随机值
    def roll(self):
        return randint(1, self.num_sides)
