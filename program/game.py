"""
game module for pig dice game

This module contains the game class which manages the main game logic,
including player turns, game flow, and win conditions for the pig dice game.
"""
from program.computer import Computer
from program.player import Player


class Game:
    """
    Represents the main game logic for pig dice game.

    The game class manages the game flow, coordinates player/computer turns,
    tracks participants, and determines when a player reaches the goal score
    to win the game. The first participant to reach 100 points wins.
    """

    # Win condition - first to reach 100 points
    GOAL = 100
    participants = []

    def __init__(self, player_1):
        """
        Initialize a new game instance.

        Sets up an empty participants list and prepares the game
        with the default goal of 100 points.
        """
        self.participants.append(player_1)

    def game(self):
        """
        Main game loop that manages the entire game flow.

        Runs the game with the given participants (players and/or computers),
        alternating turns until one participant reaches the GOAL score.
        Returns the winner when the game concludes.

        :param participants: list of Player and/or Computer objects
        :return: the winning participant
        """
        choice = input("Who do you want to play against? Another Player(p) or a Computer(c)")
        match choice:
            case "p" | "P" | "player" | "Player":
                self.participants.append(self.create_player2())
            case "C" | "c" | "computer" | "Computer":
                self.participants.append(self.create_computer())
        #self.participants.append(Computer("Clanker", 1))


        game_over = False
        player1 = self.participants[0]
        opponent = self.participants[1]
        while not game_over:
            # for participant in self.participants:
            #     if isinstance(participant, Computer):
            #         total_score = participant.take_turn()
            #     total_score = participant.take_turn()
            #     if total_score >= self.GOAL:
            #         game_over = True
            #         return participant
            game_over = player1.take_turn()
            if (player1.get_total_score()) >= self.GOAL:
                print("Goal reached! You won!")
                game_over = True
            if not game_over:
                if isinstance(opponent, Computer):
                    print(f"Computer is playing at {opponent.difficulty}")
                    opponent.take_turn(player1.get_total_score())
                else:
                    opponent.take_turn()
                if opponent.get_total_score() >= self.GOAL:
                    print("Goal reached! Opponent won")
                    game_over = True
        return player1, opponent

    def create_computer(self):
        computer_name = input("Enter the name of your enemy!")
        computer_difficulty = input("How strong is your enemy (easy, normal, hard)?")
        return Computer(computer_name, computer_difficulty)

    def create_player2(self):
        player2_name = input("Enter your name honorable player: ")
        return Player(player2_name)

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

    def quit_game(self):
        """
        Terminate the current game session.

        Ends the current game, clears the participants list, and
        prepares for a new game or exit. Does not save progress.
        """
        self.participants = []

    def restart_game(self):
        """
        Reset the current game and start fresh.

        Resets all participant scores to zero while keeping the same
        participants, allowing for a new game with the same players/computers.
        """
        for participant in self.participants:
            participant.total_score = 0

    def check_winner(self):
        """
        Check if any participant has reached the winning score.

        Iterates through all participants and returns the first one
        that has reached or exceeded the GOAL score.

        :return: winning participant or None if no winner yet
        """
        for participant in self.participants:
            if participant.total_score >= self.GOAL:
                return participant
        return None

    def get_participants(self):
        """
        Get the list of all participants in the game.

        :return: list of Player and/or Computer objects
        """
        return self.participants

    def add_participant(self, participant):
        """
        Add a new participant to the game.

        :param participant: Player or Computer object to add
        """
        self.participants.append(participant)

if __name__ == "__main__":
    player = Player("harald")
    game = Game(player)
    game.game()