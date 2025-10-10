from dice import Dice

class Computer:
    def __init__(self, computer_name, difficulty):
        self.computer_name = computer_name
        self.difficulty = difficulty
        self.id = hash(computer_name+difficulty)
        self.dice_hand = "" #create dice_hand obj once class is integrated


    def select_difficulty(self, new_difficulty):
        pass

    def change_computer_name(self, new_name):
        pass

    def roll_dice(self):
        return Dice.roll_dice()

    def hold_at_twenty(self, sum): #easy mode; replace sum w/ dice_hand sum_turn_rolls call once integrated
        while sum<20:
            roll = self.roll_dice()
            self.dice_hand = roll #call to dice_hand.add_roll_turns(roll)
            sum = self.dice_hand #call to dice_hand.sum_turn

    def four_scoring_turns(self, sum): # middle mode;
        while sum < 25:
            self.roll_dice()
        bound_hold = (100-sum)/3
        while sum < bound_hold:
            self.roll_dice()
        bound_hold = (100 - sum) / 2
        while sum < bound_hold:
            self.roll_dice()
        # self.roll_dice() until the end