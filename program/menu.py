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

    def change_username(self, old_username, new_username):
        """
        Change a player's username.

        Validates that the old username matches the current player's name,
        then updates it to the new username. The player's ID is also
        regenerated based on the new username.

        :param old_username: current username to verify
        :param new_username: new username to set
        :return: True if successful, False if old username doesn't match
        """
        if self.player1 is not None:
            if self.player1.username == old_username:
                self.player1.change_usr_name(new_username)
                return True
        return False

    def get_scoreboard(self):
        """
        Get the current scoreboard as a formatted string.

        Displays player name, current score, and progress toward the goal.
        Shows a visual representation of the player's progress using
        Unicode block characters.

        :return: formatted scoreboard string
        """
        if self.player1 is None:
            return "No player registered yet!"

        score = self.player1.total_score
        # Each block represents 10 points (max 10 blocks for 100 points)
        filled_blocks = score // 10
        empty_blocks = 10 - filled_blocks
        progress_bar = '█' * filled_blocks + '░' * empty_blocks

        scoreboard = f"""
        === SCOREBOARD ===

        Player: {self.player1.username}
        Score: {score} / 100
        Progress: {progress_bar}
        """
        return scoreboard

    def play_game(self):
        """
        Start and manage the main game flow.

        Creates a new game instance, sets up participants, and runs
        the game loop until completion. Displays the winner and final
        scores when the game ends.
        """
        # Placeholder for game logic - will be implemented with Game class
        # This method will:
        # 1. Create a Game instance
        # 2. Add participants (player1 and possibly computer)
        # 3. Run the game loop
        # 4. Display winner
        pass

    def set_player(self, player):
        """
        Set the main player for the game.

        :param player: Player object to set as player1
        """
        self.player1 = player

    def get_player(self):
        """
        Get the current player.

        :return: Player object or None if not set
        """
        return self.player1
