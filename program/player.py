"""Object Player: creates player with given name and generates unique id"""

from program.dice import Dice

# from dice_hand import DiceHand


class Player:
    """Class Player, used for real players in the game"""

    # Static variable that changes throughout all classes
    # next_id = 0

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
            self.id = hash(self.__username)  # Player.next_id
            # self._diceHand = DiceHand()
            # Player.next_id += 1
            self.__total_score = 0
        else:
            raise TypeError("name should be string!")

    def roll_dice(self):
        """Roll dice by calling dice class and saving it to player's dicehand"""
        dice = Dice.roll_dice()
        # self._diceHand.append(dice)
        return dice

    def take_turn(self):
        """
        Execute a turn for the given player or computer.

        Manages the rolling phase for a player's turn, allowing them to
        roll multiple times or hold. If a 1 is rolled, the turn ends and
        no points are scored for that turn.

        :param player: the player or computer taking their turn
        """
        temporary_score = 0
        player_continue = True
        game_over = False

        print(f"\nIts {self.__username}'s turn!")
        while player_continue:
            roll = self.roll_dice()  # method to roll the dice
            print(f"\n{self.__username} rolled a {roll}!")

            if roll == 1:
                print(f"Bad luck! {self.__username} loses all points from this turn.")
                temporary_score = 0
                player_continue = False
                break

            temporary_score += roll
            print(f"Turn score: {temporary_score}")
            player_continue, game_over = self.continue_rolling()

        self.__total_score += temporary_score
        print(f"{self.__username}'s total score: {self.__total_score}\n")
        return game_over

    def continue_rolling(self):
        choice = input(
            f"{self.__username} do you want to continue rolling (y/n)?"
        ).lower()
        if choice == "y":
            return True, False
        elif choice == "n":
            return False, False
        elif choice == "q" or "Q":
            return False, True
        else:
            print("Please enter 'y' or 'n'.")

    def change_username(self, new_name):
        """change __username (if given __username isn't empty and a string)"""
        if isinstance(new_name, (str, int, float)) and new_name != "":
            self.__username = str(new_name)
            return True
        else:
            raise TypeError("name should be string!")

    def get_username(self):
        """get access to variable __username"""
        return self.__username

    def get_id(self):
        """get access to variable id"""
        return self.id

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

    def reset(self):
        pass
