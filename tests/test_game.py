""" Unit tests for the game module. """

import pytest
from program.game import game
from tests.mock_player import MockPlayer


# ----------- __init__() -------------------------------
def test_init_creates_empty_participants_list():
    """Test that game initializes with empty participants list."""
    game_test = game()
    assert game_test.participants == []


def test_init_goal_constant():
    """Test that GOAL constant is set to 100."""
    assert game.GOAL == 100


# ----------- add_participant(self, participant) --------------
def test_add_participant_single():
    """Test adding a single participant to the game."""
    game_test = game()
    mock_player = MockPlayer("Player1", 0)

    game_test.add_participant(mock_player)

    assert len(game_test.participants) == 1
    assert game_test.participants[0] == mock_player


def test_add_participant_multiple():
    """Test adding multiple participants to the game."""
    game_test = game()
    player1 = MockPlayer("Player1", 0)
    player2 = MockPlayer("Player2", 0)

    game_test.add_participant(player1)
    game_test.add_participant(player2)

    assert len(game_test.participants) == 2
    assert game_test.participants[0] == player1
    assert game_test.participants[1] == player2


# ----------- get_participants(self) -------------------------------
def test_get_participants_empty():
    """Test getting participants when list is empty."""
    game_test = game()

    assert game_test.get_participants() == []


def test_get_participants_with_players():
    """Test getting participants when players are added."""
    game_test = game()
    player1 = MockPlayer("Player1", 0)
    player2 = MockPlayer("Player2", 0)

    game_test.add_participant(player1)
    game_test.add_participant(player2)

    participants = game_test.get_participants()
    assert len(participants) == 2
    assert player1 in participants
    assert player2 in participants


# ----------- restart_game(self) -------------------------------
def test_restart_game_resets_scores():
    """Test that restart_game resets all participant scores to 0."""
    game_test = game()
    player1 = MockPlayer("Player1", 50)
    player2 = MockPlayer("Player2", 75)

    game_test.add_participant(player1)
    game_test.add_participant(player2)

    game_test.restart_game()

    assert player1.total_score == 0
    assert player2.total_score == 0


def test_restart_game_keeps_participants():
    """Test that restart_game keeps the same participants."""
    game_test = game()
    player1 = MockPlayer("Player1", 50)
    player2 = MockPlayer("Player2", 75)

    game_test.add_participant(player1)
    game_test.add_participant(player2)

    game_test.restart_game()

    assert len(game_test.participants) == 2
    assert game_test.participants[0] == player1
    assert game_test.participants[1] == player2


def test_restart_game_empty_participants():
    """Test restart_game with no participants doesn't crash."""
    game_test = game()

    # Should not raise an error
    game_test.restart_game()
    assert game_test.participants == []


# ----------- quit_game(self) -------------------------------
def test_quit_game_clears_participants():
    """Test that quit_game clears all participants."""
    game_test = game()
    player1 = MockPlayer("Player1", 50)
    player2 = MockPlayer("Player2", 75)

    game_test.add_participant(player1)
    game_test.add_participant(player2)

    game_test.quit_game()

    assert game_test.participants == []


def test_quit_game_already_empty():
    """Test quit_game when participants list is already empty."""
    game_test = game()

    game_test.quit_game()

    assert game_test.participants == []


# ----------- check_winner(self) -------------------------------
def test_check_winner_no_winner():
    """Test check_winner when no participant has reached GOAL."""
    game_test = game()
    player1 = MockPlayer("Player1", 50)
    player2 = MockPlayer("Player2", 75)

    game_test.add_participant(player1)
    game_test.add_participant(player2)

    winner = game_test.check_winner()

    assert winner is None


def test_check_winner_one_winner():
    """Test check_winner when one participant reaches GOAL."""
    game_test = game()
    player1 = MockPlayer("Player1", 100)
    player2 = MockPlayer("Player2", 75)

    game_test.add_participant(player1)
    game_test.add_participant(player2)

    winner = game_test.check_winner()

    assert winner == player1


def test_check_winner_score_above_goal():
    """Test check_winner when participant exceeds GOAL."""
    game_test = game()
    player1 = MockPlayer("Player1", 120)

    game_test.add_participant(player1)

    winner = game_test.check_winner()

    assert winner == player1


def test_check_winner_empty_participants():
    """Test check_winner with no participants."""
    game_test = game()

    winner = game_test.check_winner()

    assert winner is None


def test_check_winner_multiple_winners():
    """Test check_winner returns first winner when multiple reach GOAL."""
    game_test = game()
    player1 = MockPlayer("Player1", 100)
    player2 = MockPlayer("Player2", 105)

    game_test.add_participant(player1)
    game_test.add_participant(player2)

    winner = game_test.check_winner()

    assert winner == player1  # First winner is returned


# ----------- speedrun_game(self) -------------------------------
def test_speedrun_game_sets_first_participant_score():
    """Test that speedrun_game sets first participant's score near GOAL."""
    game_test = game()
    player1 = MockPlayer("Player1", 0)

    game_test.add_participant(player1)

    game_test.speedrun_game()

    assert player1.total_score == game.GOAL - 10


def test_speedrun_game_only_affects_first_participant():
    """Test that speedrun_game only modifies first participant."""
    game_test = game()
    player1 = MockPlayer("Player1", 0)
    player2 = MockPlayer("Player2", 0)

    game_test.add_participant(player1)
    game_test.add_participant(player2)

    game_test.speedrun_game()

    assert player1.total_score == game.GOAL - 10
    assert player2.total_score == 0


def test_speedrun_game_empty_participants():
    """Test speedrun_game with no participants doesn't crash lol."""
    game_test = game()

    # Should not raise an error
    game_test.speedrun_game()
    assert game_test.participants == []


# ----------- game(self, participants) -------------------------------
def test_game_sets_participants():
    """Test that game() method sets participants list."""
    game_test = game()
    player1 = MockPlayer("Player1", 100)
    player2 = MockPlayer("Player2", 0)
    participants = [player1, player2]

    winner = game_test.game(participants)

    assert game_test.participants == participants
    assert winner == player1


def test_game_returns_winner_when_goal_reached():
    """Test that game() returns winner when GOAL is reached."""
    game_test = game()
    player1 = MockPlayer("Player1", 100)
    player2 = MockPlayer("Player2", 0)
    participants = [player1, player2]

    winner = game_test.game(participants)

    assert winner == player1


def test_game_empty_participants_list():
    """Test game() with empty participants list."""
    game_test = game()
    participants = []

    winner = game_test.game(participants)

    assert winner is None


# ----------- Integration tests -------------------------------
def test_full_game_flow():
    """Test complete game flow from start to finish."""
    game_test = game()
    player1 = MockPlayer("Player1", 0)
    player2 = MockPlayer("Player2", 0)

    game_test.add_participant(player1)
    game_test.add_participant(player2)

    # Simulate game progress
    player1.total_score = 100

    winner = game_test.check_winner()

    assert winner == player1
    assert len(game_test.participants) == 2


def test_restart_after_game():
    """Test that game can be restarted after completion."""
    game_test = game()
    player1 = MockPlayer("Player1", 100)
    player2 = MockPlayer("Player2", 75)

    game_test.add_participant(player1)
    game_test.add_participant(player2)

    winner = game_test.check_winner()
    assert winner == player1

    game_test.restart_game()

    assert player1.total_score == 0
    assert player2.total_score == 0
    assert len(game_test.participants) == 2


def test_speedrun_then_check_winner():
    """Test using speedrun and then checking for winner."""
    game_test = game()
    player1 = MockPlayer("Player1", 0)

    game_test.add_participant(player1)
    game_test.speedrun_game()

    # Player1 should be at 90, not a winner yet
    winner = game_test.check_winner()
    assert winner is None

    # Add 10 more points to win
    player1.total_score = 100
    winner = game_test.check_winner()
    assert winner == player1
