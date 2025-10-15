"""
computer module
"""

from dice import Dice
from dice_hand import DiceHand


class Computer:
    """
    computer player class with three different difficulty modes
    methods:
        __init__(computer_name, difficulty),
        select_difficulty(new_difficulty),
        change_computer_name(new_name),
        roll_dice()-->static,
        hold_at_twenty() --> easy mode,
        scoring_turn() --> normal mode,
        keep_or_race(player_score) --> hard mode,
        take_turn(player_score) --> should be only call really outside the class
    """

    def __init__(self, computer_name, difficulty):
        """Constructor"""
        self.computer_name = computer_name
        self.difficulty = difficulty  # has to be a tuple
        self.id = hash(computer_name + difficulty)
        self.dice_hand = DiceHand()  # create dice_hand obj once class is integrated
        self.score = 0
        self.turn_number = 0  # number of scoring turns

    def select_difficulty(self, new_difficulty):
        """selecting new difficulty;"""
        if new_difficulty in ("easy", 1):  # from linting lol
            self.difficulty = (1, "easy")
        elif new_difficulty in ("normal", 2):
            self.difficulty = (2, "normal")
        elif new_difficulty in ("hard", 3):
            self.difficulty = (3, "hard")
        else:
            return f"Invalid Difficulty Option: {new_difficulty}"
        return f"Difficulty changed to: {self.difficulty[1]}"

    def change_computer_name(self, new_name):
        """changing the computer username, id remains the same"""
        if not new_name == "":
            self.computer_name = new_name
        else:
            return "Name is invalid or/and null"
        return ""

    def roll_dice(self):
        """rolls the dice; make it static?"""
        return Dice.roll_dice()

    def hold_at_twenty(self):  # easy mode;
        """
        Each turn try to reach the sum of 20;
        https://en.wikipedia.org/wiki/Pig_(dice_game)#Optimal_play
        :return: the result of the turn, either sum of the dice
         or 0 (when a 1 is rolled)
        """
        turn = 0
        roll_is_one = False

        while not roll_is_one and turn < 20:
            roll = self.roll_dice()
            if roll == 1:
                roll_is_one = True
                turn = 0
                self.dice_hand.reset_turn_list()
            else:
                self.dice_hand.add_roll(roll)
                turn += roll
        return turn

    def scoring_turn(self):  # normal mode
        """
        4 scoring turns,
        bound--> sum trying to be reached each turn
        1. turn: bound = 25, sum1
        2. turn: bound = (100-sum1)/3, sum2
        3. turn: bound = (100-sum2)/2, sum3
        4. turn: bound = (100-sum3), sum4>=100
        :return: 0 (rolled a 1) or sum( var turn)
        """
        # setup
        turn = 0
        if self.turn_number == 0:
            # incorrect logic, should be 4, see docstring
            # double check
            bound = 25
        else:
            bound = (100 - self.score) / self.turn_number
        roll_is_one = False

        # turn
        while not roll_is_one and turn < bound:
            roll = Dice.roll_dice()
            if roll == 1:
                roll_is_one = True
                turn = 0
                self.dice_hand.reset_turn_list()
            else:
                turn += roll
                self.dice_hand.add_roll(roll)

        # end of turn logic
        if not roll_is_one:
            self.turn_number += 1
            self.dice_hand.add_turn_rolls()
        return turn

    def keep_or_race(self, player_score):  # hard mode
        """
        if the player score or the computers score is below 71, roll to win
        Otherwise, hold on 21 plus the difference between scores divided by 8
        bound = 21 + (|player_score-self.score|)/8
        :param player_score: requires player_score for an if statement
        :return: 0 (rolled a 1) or sum( var turn)
        """
        turn = 0
        roll_is_one = False

        if (player_score or self.score) < 71:
            while (
                not roll_is_one and 21 + (player_score - self.score) / 8
            ):  # absolute score
                roll = self.roll_dice()
                if roll == 1:
                    roll_is_one = True
                    turn = 0
                    self.dice_hand.reset_turn_list()
                else:
                    self.dice_hand.add_roll(roll)
                    turn += roll
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

    def take_turn(self, player_score=0):
        """
        turn method, should be the only function called outside the class,
        besides init and change_computer_name(...)
        :param player_score: for keep_or_race function
        :return: turn (sum or 0)
        """
        turn = 0
        match self.difficulty[0]:
            case 1:
                turn = self.hold_at_twenty()
            case 2:
                turn = self.scoring_turn()
            case 3:
                turn = self.keep_or_race(player_score)
        return turn
