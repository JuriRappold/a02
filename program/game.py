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

    def game(self, participants):
        """
        Main game loop that manages the entire game flow.

        Runs the game with the given participants (players and/or computers),
        alternating turns until one participant reaches the GOAL score.
        Returns the winner when the game concludes.

        :param participants: list of Player and/or Computer objects
        :return: the winning participant
        """
        self.participants = participants
        game_over = False

        while not game_over:
            for participant in self.participants:
                self.turn(participant)
                if participant.total_score >= self.GOAL:
                    game_over = True
                    return participant
        return None

    def speedrun_game(self):
        """
        Cheat mode for rapid game completion and testing.

        Automatically advances the game quickly by either setting player
        scores to near-winning values or simulating rapid turns.
        Useful for testing end-game scenarios without playing through.
        """
        if len(self.participants) > 0:
            # Set first participant's score to just below goal for quick win
            self.participants[0].total_score = self.GOAL - 10
