"""
game module for pig dice game

This module contains the game class which manages the main game logic,
including player turns, game flow, and win conditions for the pig dice game.
"""


class game:
    """
    Represents the main game logic for pig dice game.

    The game class manages the game flow, coordinates player/computer turns,
    tracks participants, and determines when a player reaches the goal score
    to win the game.
    """

    GOAL = 100

    def __init__(self):
        """
        Initialize a new game instance.

        Sets up an empty participants list and prepares the game
        with the default goal of 100 points.
        """
        self.participants = []

    def turn(self, player):
        """
        Execute a turn for the given player or computer.

        Manages the rolling phase for a player's turn, allowing them to
        roll multiple times or hold. If a 1 is rolled, the turn ends and
        no points are scored for that turn.

        :param player: the player or computer taking their turn
        """

        pass
