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
        self.game_rules = ""
        self.player1 = None
