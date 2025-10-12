"""
menu module for pig dice game

This module contains the menu class which provides the user interface
for the pig dice game, including game setup, player management, and
displaying game information.
"""


class menu:
    """
    Manages the user interface and menu system for pig dice game.

    The menu class handles user interactions, displays game rules,
    manages player information, shows scoreboards, and initiates games.
    Acts as the main entry point for player interaction.
    """

    def __init__(self):
        """
        Initialize a new menu instance.

        Sets up default game rules and initializes player1 to None.
        The player will be created during the game setup phase.
        """
        self.game_rules = self._initialize_rules()
        self.player1 = None

    def _initialize_rules(self):
        """
        Initialize the game rules string with pig dice rules.

        :return: formatted string containing the game rules
        """
        rules = """
        === PIG DICE GAME RULES ===

        OBJECTIVE: Be the first player to reach 100 points!

        GAMEPLAY:
        - On your turn, roll the dice as many times as you want
        - Each roll adds to your turn total
        - You can choose to 'hold' and add your turn total to your score
        - BUT if you roll a 1, you lose all points for that turn!

        STRATEGY:
        - Risk vs Reward: Keep rolling for more points or hold to secure them?
        - The choice is yours!

        WIN CONDITION: First to 100 points wins!
        """
        return rules

    def get_rules(self):
        """
        Get the game rules as a formatted string.

        Returns the complete rules of the pig dice game for display
        to the player.

        :return: string containing the game rules
        """
        return self.game_rules
