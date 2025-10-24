"""
menu module for pig dice game

This module contains the menu class which provides the user interface
for the pig dice game, including game setup, player management, and
displaying game information. The menu acts as the main interaction
point between the player and the game.
"""
from program.game import Game


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
        ========================================================
                    PIG DICE GAME RULES
        ========================================================

        OBJECTIVE:
          Be the first player to reach 100 points!

        GAMEPLAY:
          • Roll the dice as many times as you want
          • Each roll adds to your turn total
          • Choose 'HOLD' to bank your points
          • BUT... rolling a 1 loses ALL turn points!

        STRATEGY:
          Risk vs Reward - When do you hold?
          The more you roll, the bigger the risk!

        WIN CONDITION:
          First to 100 points wins!

        ========================================================
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

        if old_username is None:
            return False

        if self.player1 is not None:
            if self.player1.username == old_username:
                # Validate new_username
                if new_username is None:
                    return False
                # Only allow str, int, float types
                if not isinstance(new_username, (str, int, float)):
                    return False
                # Convert to string for uniform validation
                new_username_str = str(new_username)
                # Reject if username contains newlines
                if '\n' in new_username_str:
                    return False
                new_username = new_username_str
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
        progress_bar = "█" * filled_blocks + "░" * empty_blocks

        scoreboard = f"""
        ========================================================
                         SCOREBOARD
        ========================================================

        Player: {self.player1.username}
        Score:  {score} / 100

        Progress: [{progress_bar}]

        ========================================================
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
        game = Game(self.player1)
        game.game()

    def set_player(self, player):
        """
        Set the main player for the game.

        :param player: Player object to set as player1
        :return: True if successful, False if invalid input
        """
        # Validate input - must be an object with username attribute
        if player is None:
            return False
        if not hasattr(player, 'username'):
            return False

        self.player1 = player
        return True

    def set_computer():
        pass

    def get_player(self):
        """
        Get the current player.

        :return: Player object or None if not set
        """
        return self.player1

    def display_welcome(self):
        """
        Display welcome message for the game.

        Shows an ASCII art welcome screen and brief game introduction.

        :return: formatted welcome message string
        """
        welcome = """
        ========================================================

                 WELCOME TO PIG DICE GAME!

                 Roll the dice, take your chances!
                 First to 100 points wins!

                 Good luck and have fun!

        ========================================================
        """
        return welcome

    def display_menu_options(self):
        """
        Display main menu options to the player.

        :return: formatted menu options string
        """
        # missing changing difficulty for computer
        options = """
        ========================================
                    MAIN MENU
        ========================================

          1. Play Game
          2. View Rules
          3. View Scoreboard
          4. Change Username
          5. Quit

        ========================================

        Enter your choice: """
        return options

    def validate_menu_choice(self, choice):
        """
        Validate if the menu choice is valid.

        :param choice: user input choice (string)
        :return: True if choice is valid (1-5), False otherwise
        :raises ValueError: if choice cannot be converted to int or is invalid
        """
        try:
            # Reject floats explicitly
            if isinstance(choice, float):
                raise ValueError("False: Invalid menu choice: must be an integer between 1 and 5")
            choice_int = int(choice)
            if not (1 <= choice_int <= 5):
                raise ValueError("False: Invalid menu choice: must be an integer between 1 and 5")
            return True
        except (ValueError, TypeError):
            raise ValueError("False: Invalid menu choice: must be an integer between 1 and 5")

    def display_error_message(self, message):
        """
        Display an error message to the user.

        :param message: error message to display
        :return: formatted error message string
        """
        return f"\n  ❌ ERROR: {message}\n"

    def display_success_message(self, message):
        """
        Display a success message to the user.

        :param message: success message to display
        :return: formatted success message string
        """
        return f"\n  ✅ SUCCESS: {message}\n"
