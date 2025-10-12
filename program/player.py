"""
player module for pig dice game

This module contains the player class which represents a player in the game.
Each player has a username, unique ID, total score, and a dice hand.
"""


class player:
    """
    Represents a player in the pig dice game.

    The player class manages player information including username,
    unique player ID (generated from username hash), total score across games,
    and the player's dice hand for the current game.
    """
    
    def __init__(self, username):
        """
        Initialize a new player with the given username.
        
        :param username: the player's username (String)
        """
        self.username = username
        self.player_ID = hash(username)
        self.total_score = 0
        self.dice_hand = None

    def roll_dice(self):
        """
        Roll the dice for this player's current turn.

        This method triggers a dice roll using the player's dice hand.
        The dice hand manages the actual rolling logic and stores the results.
        """
        if self.dice_hand is not None:
            self.dice_hand.roll_dice()

