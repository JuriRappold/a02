"""Module for class DiceHand."""


class DiceHand:  # change class name to Dice_Hand???
    """Keeps track of every roll a player makes over the entire game."""

    def __init__(self):
        """DiceHand Constructor, creates empty lists."""
        self.game_rolls = []
        self.turn_rolls = []
        print(type(self))

    def add_turn_rolls(self):
        """Adds the rolls of an entire turn to the list of rolls of the game for an individual player.

        :return: NaN
        """
        # self.game_rolls.append(self.turn_rolls)#!!!appends list as list item!!
        for r in self.turn_rolls:
            self.game_rolls.append(r)
        self.turn_rolls = []

    def add_roll(self, roll):
        """Adds the current roll to a temporary turn list of rolls.

        :param roll: has to be an integer, else it raises a TypeError
        :return: NaN
        """
        if isinstance(roll, int):
            if 1 <= roll <= 6:
                self.turn_rolls.append(roll)
        else:
            raise TypeError("Roll not an int; Check dice_hand .add_roll() calls")

    def sum_game_rolls(self):
        """Sum of the list of game rolls.

        :return: sum
        """
        sum_rolls = 0
        for r in self.game_rolls:
            sum_rolls += r
        return sum_rolls

    def sum_turn_rolls(self):
        """Sum of the list for the turn.

        :return:
        """
        sum_rolls = 0
        for r in self.turn_rolls:
            sum_rolls += r
        return sum_rolls

    def reset_turn_list(self):
        """
        Resets the turn list, in case somebody rolled a one.

        :return:
        """
        self.turn_rolls = []
