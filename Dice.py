from random import randint


class Dice:
    """
    Dice class which is responsible for rolling and get the output.
    """

    def __init__(self, count: int = 1):
        self.dice_count = count

    def roll_dice(self):
        """
        it will roll the dice and get the output on the basis of the number of dice.
        :return: None
        """
        output = 0
        count = self.dice_count
        while count > 0:
            output += randint(1, 6)
            count -= 1
        return output
