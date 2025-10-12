from dice import Dice
from dice_hand import DiceHand

class Computer:
    def __init__(self, computer_name, difficulty):
        self.computer_name = computer_name
        self.difficulty = difficulty
        self.id = hash(computer_name+difficulty)
        self.dice_hand = DiceHand() #create dice_hand obj once class is integrated
        self.score = 0


    def select_difficulty(self, new_difficulty):
        pass

    def change_computer_name(self, new_name):
        pass

    def roll_dice(self):
        return Dice.roll_dice()

    def hold_at_twenty(self): #easy mode; replace sum w/ dice_hand sum_turn_rolls call once integrated
        sum = 0
        while sum<20:
            roll = self.roll_dice()
            #print(type(roll))
            #print(isinstance(roll, int))
            self.dice_hand.add_roll(roll) #call to dice_hand.add_roll_turns(roll)
            sum += roll#self.dice_hand.sum_turn_rolls() #call to dice_hand.sum_turn
        return sum

    def four_scoring_turns(self): # middle mode;
        # while sum < 25:
        #     self.roll_dice()
        # bound_hold = (100-sum)/3
        # while sum < bound_hold:
        #     self.roll_dice()
        # bound_hold = (100 - sum) / 2
        # while sum < bound_hold:
        #     self.roll_dice()
        # # self.roll_dice() until the end
        # while sum < 100:
        #     self.roll_dice()
        sum = 0
        if self.score < 25:
            while (self.score + sum) <25:
                roll = self.roll_dice()
                self.dice_hand.add_roll(roll)
                sum += roll
        # elif (100-self.score)/3:
        #     while (self.score +sum) <

    def keep_or_race(self, player_score): #hard mode
        sum = 0
        if (player_score or self.score) < 71:
            while 21 + (player_score-self.score)/8:
                roll = self.roll_dice()
                self.dice_hand.add_roll(roll)
                sum+=roll
        else:
            while (self.score + sum) < 100:
                roll = self.roll_dice()
                self.dice_hand.add_roll(roll)
                sum += roll
        return sum


# myComputer = Computer("myComputer", "easy")
# for myComputer.score in range(100):
#     print("Loop:")
#     print(myComputer.score)
#     myComputer.score += myComputer.hold_at_twenty()
#     print(f"Sum: {myComputer.score}")
#     print("End Loop;")