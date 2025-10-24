"""computer module."""

from program.dice import Dice
from program.dice_hand import DiceHand


class Computer:
    """computer player class with three different difficulty modes.

    methods:
    __init__(__username, difficulty),
    select_difficulty(new_difficulty),
    change_computer_name(new_name),
    roll_dice()-->static,
    hold_at_twenty() --> easy mode,
    scoring_turn() --> normal mode,
    keep_or_race(player_score) --> hard mode,
    take_turn(player_score) -->
    should be only call really outside the class
    """

    __DIFFICULTIES = [(1, "easy"), (2, "normal"), (3, "hard")]
    __DEFAULT_NAME = "Harald (default)"

    def __init__(self, computer_name, difficulty):
        """Computer Constructor with input checks."""
        self.__username = self.check_valid_computer_name(computer_name)
        self.difficulty = self.check_valid_difficulty(difficulty)
        self.id = hash(str(computer_name) + str(self.difficulty))
        self.dice_hand = DiceHand()
        self.total_score = 0
        self.turn_number = 4  # number of scoring turns needed

    def select_difficulty(self, new_difficulty):
        """Selects new difficulty."""
        self.difficulty = self.check_valid_difficulty(new_difficulty)
        return f"Difficulty changed to: {self.__DIFFICULTIES[self.difficulty][1]}"

    def change_computer_name(self, new_name):
        """Changes the computer __username, id remains the same."""
        self.__username = self.check_valid_computer_name(new_name)

    def roll_dice(self):
        """Rolls the dice; make it static?."""
        return Dice.roll_dice()

    def hold_at_twenty(self):  # easy mode;
        """Each turn try to reach the sum of 20.

        https://en.wikipedia.org/wiki/Pig_(dice_game)#Optimal_play
        :return: the result of the turn, either sum of the dice
         or 0 (when a 1 is rolled)
        """
        turn = 0
        roll_is_one = False

        while not roll_is_one and turn < 20:
            roll = self.roll_dice()
            print(f"roll: {roll}")
            if roll == 1:
                roll_is_one = True
                turn = 0
                self.dice_hand.reset_turn_list()
            else:
                self.dice_hand.add_roll(roll)
                turn += roll
        print(f"turn: {turn}")
        return turn

    def scoring_turn(self):  # normal mode
        """4 scoring turns.

        bound--> sum trying to be reached each turn
        1. turn: bound = 25, sum1
        2. turn: bound = (100-sum1)/3, sum2
        3. turn: bound = (100-sum2)/2, sum3
        4. turn: bound = (100-sum3), sum4>=100
        :return: 0 (rolled a 1) or sum( var turn)
        """
        # setup
        turn = 0
        if self.turn_number == 4:
            # incorrect logic, should be 4, see docstring
            # double check
            bound = 25
        else:
            bound = (100 - self.total_score) / self.turn_number
        roll_is_one = False

        # turn
        while not roll_is_one and turn < bound:
            roll = Dice.roll_dice()
            print(f"Roll{roll}")
            if roll == 1:
                roll_is_one = True
                turn = 0
                self.dice_hand.reset_turn_list()
            else:
                turn += roll
                self.dice_hand.add_roll(roll)
            print(f"Turn: {turn}")

        # end of turn logic
        if not roll_is_one:
            self.turn_number -= 1
            self.dice_hand.add_turn_rolls()
        return turn

    def keep_or_race(self, player_score):  # hard mode
        """If the player score or the computers score is below 71, roll to win.

        Otherwise, hold on 21 plus the difference between scores divided by 8
        bound = 21 + (|player_score-self.score|)/8
        :param player_score: requires player_score for an if statement
        :return: 0 (rolled a 1) or sum( var turn)
        """
        turn = 0
        roll_is_one = False

        if (player_score or self.total_score) < 71:
            while (
                not roll_is_one and 21 + (player_score - self.total_score) / 8
            ):  # absolute score
                roll = self.roll_dice()
                print(f"Roll: {roll}")
                if roll == 1:
                    roll_is_one = True
                    turn = 0
                    self.dice_hand.reset_turn_list()
                else:
                    self.dice_hand.add_roll(roll)
                    turn += roll
                print(f"turn score: {turn}")
        else:
            while not roll_is_one and (self.total_score + turn) < 100:
                roll = self.roll_dice()
                print(f"Roll: {roll}")
                if roll == 1:
                    roll_is_one = True
                    turn = 0
                else:
                    self.dice_hand.add_roll(roll)
                    turn += roll
                print(f"turn score: {turn}")
        return turn

    def take_turn(self, player_score=0):
        """Turn method, should be the only function called outside the class.

        besides init and change_computer_name(...)
        :param player_score: for keep_or_race function
        :return: turn (sum or 0)
        """
        turn = 0
        diff = self.__DIFFICULTIES[self.difficulty]
        match diff[0]:
            case 1:
                print("easy")
                turn = self.hold_at_twenty()
            case 2:
                print("normal")
                turn = self.scoring_turn()
            case 3:
                print("hard")
                turn = self.keep_or_race(player_score)
        self.total_score += turn
        print(f"total score: {self.total_score}")
        return turn

    def check_valid_computer_name(self, computer_name):
        """Checks if the __username is of a valid type.

         and returns a valid __username
        1. of type string:
            "" str --> default_name
            else: return __username
        2. of type list --> concatenate list elements into a string
        3. of type dict --> concatenate dict values into a string
        4. else return default
        """
        if computer_name is None:
            return self.__DEFAULT_NAME

        if isinstance(computer_name, str):
            if computer_name == "":
                return self.__DEFAULT_NAME
            return computer_name
        if isinstance(computer_name, list):
            new_name = ""
            for item in computer_name:
                new_name += str(item)
            return new_name
        if isinstance(computer_name, dict):
            new_name = ""
            for values in computer_name.values():
                new_name += str(values)
            return new_name
        return self.__DEFAULT_NAME

    def check_valid_difficulty(self, difficulty):
        """
        Checks types of difficulty.

        :param difficulty: valid index (int) or
         valid string ("easy", "normal", "hard")
        :return: proper index value of self.__DIFFICULTIES
        for the entered difficulty
        """
        list_diff = []
        for diff in self.__DIFFICULTIES:
            list_diff.append(diff[1])

        if isinstance(difficulty, int or float):
            difficulty = int(difficulty)
            if 0 <= difficulty <= 2:
                return difficulty
            raise IndexError("Index Error Out of Bounds")

        if isinstance(difficulty, str):
            if difficulty not in list_diff:
                raise ValueError("value is a non-valid string")
            match difficulty:
                case "easy":
                    return 0
                case "normal":
                    return 1
                case "hard":
                    return 2
        if difficulty is None or isinstance(difficulty, list | dict | tuple | Computer):
            raise TypeError(f"type is {type(difficulty)}")
        return 0

    def get_total_score(self):
        return self.total_score

    def get_username(self):
        return self.__username
