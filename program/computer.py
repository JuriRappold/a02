from dice import Dice
from dice_hand import DiceHand

class Computer:
    def __init__(self, computer_name, difficulty):
        self.computer_name = computer_name
        self.difficulty = difficulty #has to be a tuple
        self.id = hash(computer_name+difficulty)
        self.dice_hand = DiceHand() #create dice_hand obj once class is integrated
        self.score = 0
        self.turn_number = 0 #number of scoring turns


    def select_difficulty(self, new_difficulty):
        if new_difficulty == "easy" or new_difficulty==1:
           self.difficulty = (1, "easy")
        elif new_difficulty == "normal" or new_difficulty==2:
            self.difficulty = (2, "normal")
        elif new_difficulty == "hard" or new_difficulty == 3:
            self.difficulty = (3, "hard")
        else:
            return "Invalid Difficulty Option"
        return f"Difficulty changed to: {self.difficulty[1]}"

    def change_computer_name(self, new_name):
        if not new_name == "":
            self.computer_name = new_name
        else:
            return "Name is invalid or/and null"

    def roll_dice(self):
        return Dice.roll_dice()

    def hold_at_twenty(self): #easy mode;
        turn = 0
        roll_is_one = False

        while not roll_is_one and turn<20:
            roll = self.roll_dice()
            if roll == 1:
                roll_is_one = True
                turn = 0
                self.dice_hand.reset_turn_list()
            else:
                self.dice_hand.add_roll(roll)
                turn += roll
        return turn

    def scoring_turn(self):
        #setup
        turn = 0
        if self.turn_number == 0:
            bound = 25
        else:
            bound = (100-self.score)/self.turn_number
        roll_is_one = False

        #turn
        while not roll_is_one and turn < bound:
            roll = Dice.roll_dice()
            if roll == 1:
                roll_is_one = True
                turn = 0
                self.dice_hand.reset_turn_list()
            else:
                turn += roll
                self.dice_hand.add_roll(roll)

        #end of turn logic
        if not roll_is_one:
            self.turn_number+=1
            self.dice_hand.add_turn_rolls()
        return turn

    def keep_or_race(self, player_score): #hard mode
        turn = 0
        roll_is_one = False

        if (player_score or self.score) < 71:
            while not roll_is_one and 21 + (player_score-self.score)/8:
                roll = self.roll_dice()
                if roll == 1:
                    roll_is_one = True
                    turn = 0
                else:
                    self.dice_hand.add_roll(roll)
                    turn+=roll
        else:
            while not roll_is_one and (self.score + turn) < 100:
                roll = self.roll_dice()
                if roll == 1:
                    roll_is_one = True
                    turn = 0
                else:
                    self.dice_hand.add_roll(roll)
                    turn += roll
        return turn
