

class DiceHand:
    """
    keeps track of every roll a player makes over the entire game
    """
    # Attributes
    #game_rolls = []
    #turn_rolls = []

    # Methods
    def __init__(self):
        # declare attributes here, not above?
        self.game_rolls =[]
        self.turn_rolls = []

    def add_turn_rolls(self):
        """
        adds the rolls of an entire turn to the list of rolls of the game for an individual player
        :return: NaN
        """
        self.game_rolls.append(self.turn_rolls) #!!!appends list as list item!!
        self.turn_rolls = []

    def add_roll(self, roll):
        """
        adds the current roll to a temporary turn list of rolls
        :param roll: has to be an integer, else it raises a TypeError
        :return: NaN
        """
        if isinstance(roll, int):
            self.turn_rolls.append(roll)
        raise TypeError("Roll not an int; Check where Obj<DiceHand>.add_roll(roll) is called (Probably in Player)")
