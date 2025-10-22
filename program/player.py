"""Object Player: creates player with given name and generates unique id"""

from program.dice import Dice

# from dice_hand import DiceHand


class Player:
    """Class Player, used for real players in the game"""

    # Static variable that changes throughout all classes
    next_id = 0

    def __init__(self, name):
        """Initialisation of object Player.
        If name is string and not an empty string, we create an object that has: <br>
        1. Username<br>
        2. Unique id<br>
        3. Total score (that will be changed throughout the game)<br>
        4. DiceHand obj, that stores all rolled dice
        """
        if isinstance(name, str) and name != "":
            self.__username = name
            self.__player_id = Player.next_id
            # self._diceHand = DiceHand()
            Player.next_id += 1
            self.__total_score = 0
        else:
            raise TypeError("name should be string!")

    def roll_dice(self):
        """Roll dice by calling dice class and saving it to player's dicehand"""
        dice = Dice.roll_dice()
        # self._diceHand.append(dice)
        return dice

    def change_username(self, new_name):
        """change username (if given username isn't empty and a string)"""
        if isinstance(new_name, str) and new_name != "":
            self.__username = new_name
        else:
            raise TypeError("name should be string!")

    def get_username(self):
        """get access to variable username"""
        return self.__username

    def get_id(self):
        """get access to variable id"""
        return self.__player_id

    def get_total_score(self):
        """get access to variable total score"""
        return self.__total_score

    # for cheating purposes
    def set_total_score(self, score):
        """For cheating/testing purposes: set total_score to other value"""
        self.__total_score = score

    def set_dice_hand(self, dice_hand_list):
        """For cheating/testing purposes: set dice_hand_list to other value"""
        # self.diceHand = dice_hand_list
