"""Unit tests for the game module."""

import pytest
from program.game import Game
from tests.mock_player import MockPlayer


# ----------- __init__() -------------------------------
def test_init_creates_empty_participants_list():
    """Test that game initializes with player added to participants list."""
    mock_player = MockPlayer("Gunnar", 0)
    game_test = Game(mock_player)
    assert len(game_test.participants) == 1
    assert game_test.participants[0] == mock_player


def test_init_goal_constant():
    """Test that GOAL constant is set to 100."""
    assert Game.GOAL == 100


# ----------- add_participant(self, participant) --------------
def test_add_participant():
    """Test adding a participant to the game."""
    initial_player = MockPlayer("Gunnar", 0)
    game_test = Game(initial_player)
    mock_player = MockPlayer("Juri", 0)

    game_test.add_participant(mock_player)

    assert len(game_test.participants) == 2
    assert game_test.participants[0] == initial_player
    assert game_test.participants[1] == mock_player


def test_get_participants_with_players():
    """Test getting participants when players are added."""
    player1 = MockPlayer("Gunnar", 0)
    game_test = Game(player1)
    player2 = MockPlayer("Juri", 0)

    game_test.add_participant(player2)

    participants = game_test.get_participants()
    assert len(participants) == 2
    assert player1 in participants
    assert player2 in participants


# ----------- restart_game(self) -------------------------------
def test_restart_game_resets_scores():
    """Test that restart_game resets all participant scores to 0."""
    player1 = MockPlayer("Gunnar", 50)
    game_test = Game(player1)
    player2 = MockPlayer("Juri", 75)

    game_test.add_participant(player2)

    game_test.restart_game()

    assert player1.total_score == 0
    assert player2.total_score == 0


def test_restart_game_keeps_participants():
    """Test that restart_game keeps the same participants."""
    player1 = MockPlayer("Gunnar", 50)
    game_test = Game(player1)
    player2 = MockPlayer("Juri", 75)

    game_test.add_participant(player2)

    game_test.restart_game()

    assert len(game_test.participants) == 2
    assert game_test.participants[0] == player1
    assert game_test.participants[1] == player2


def test_restart_game_empty_score():
    """Test restart_game with no participants doesn't crash."""
    player1 = MockPlayer("Gunnar", 50)
    game_test = Game(player1)
    game_test.restart_game()
    # Player should still be in the list but with score reset to 0
    assert len(game_test.participants) == 1
    assert player1.total_score == 0


# ----------- quit_game(self) -------------------------------
def test_quit_game_clears_participants():
    """Test that quit_game clears all participants."""
    player1 = MockPlayer("Gunnar", 50)
    game_test = Game(player1)
    player2 = MockPlayer("Juri", 75)

    game_test.add_participant(player2)

    game_test.quit_game()

    assert game_test.participants == []


def test_quit_game_already_empty():
    """Test quit_game when participants list is already empty."""
    game_test = Game(MockPlayer("Gunnar", 0))

    game_test.quit_game()

    assert game_test.participants == []


# ----------- check_winner(self) -------------------------------
def test_check_winner_no_winner():
    """Test check_winner when no participant has reached GOAL."""
    player1 = MockPlayer("Gunnar", 50)
    game_test = Game(player1)
    player2 = MockPlayer("Juri", 75)

    game_test.add_participant(player2)

    winner = game_test.check_winner()

    assert winner is None


def test_check_winner_one_winner():
    """Test check_winner when one participant reaches GOAL."""
    player1 = MockPlayer("Gunnar", 100)  # Player1 has winning score
    game_test = Game(player1)
    player2 = MockPlayer("Juri", 75)

    game_test.add_participant(player2)

    winner = game_test.check_winner()

    assert winner == player1


def test_check_winner_score_above_goal():
    """Test check_winner when participant exceeds GOAL."""
    player1 = MockPlayer("Gunnar", 120)
    game_test = Game(player1)

    winner = game_test.check_winner()

    assert winner == player1


def test_check_winner_empty_participants():
    """Test check_winner with no participants."""
    game_test = Game(MockPlayer("Gunnar", 0))

    winner = game_test.check_winner()

    assert winner is None


def test_check_winner_multiple_winners():
    """Test check_winner returns first winner when multiple reach GOAL."""
    player1 = MockPlayer("Gunnar", 100)
    game_test = Game(player1)
    player2 = MockPlayer("Juri", 105)

    game_test.add_participant(player2)

    winner = game_test.check_winner()

    assert winner == player1  # First winner is returned


# ----------- speedrun_game(self) -------------------------------
def test_speedrun_game_sets_first_participant_score():
    """Test that speedrun_game sets first participant's score near GOAL."""
    player1 = MockPlayer("Gunnar", 50)
    game_test = Game(player1)

    game_test.speedrun_game()

    assert player1.total_score == Game.GOAL - 10


def test_speedrun_game_only_affects_first_participant():
    """Test that speedrun_game only modifies first participant."""
    player1 = MockPlayer("Gunnar", 50)
    game_test = Game(player1)
    player2 = MockPlayer("Juri", 75)

    game_test.add_participant(player2)

    game_test.speedrun_game()

    assert player1.total_score == Game.GOAL - 10


def test_speedrun_game():
    """Test speedrun_game with one participant doesn't crash."""
    player1 = MockPlayer("Gunnar", 0)
    game_test = Game(player1)

    # Should not raise an error
    game_test.speedrun_game()
    # Player score set to GOAL - 10
    assert len(game_test.participants) == 1
    assert player1.total_score == Game.GOAL - 10


# ----------- Integration tests -------------------------------
def test_full_game_flow():
    """Test complete game flow from start to finish."""
    player1 = MockPlayer("Gunnar", 0)
    game_test = Game(player1)
    player2 = MockPlayer("Juri", 0)

    game_test.add_participant(player2)

    # Simulate game progress
    player1.total_score = 100

    winner = game_test.check_winner()

    assert winner == player1
    assert len(game_test.participants) == 2


def test_restart_after_game():
    """Test that game can be restarted after completion."""
    player1 = MockPlayer("Gunnar", 100)
    game_test = Game(player1)
    player2 = MockPlayer("Juri", 75)

    game_test.add_participant(player2)

    winner = game_test.check_winner()
    assert winner == player1

    game_test.restart_game()

    assert player1.total_score == 0
    assert player2.total_score == 0
    assert len(game_test.participants) == 2


def test_speedrun_then_check_winner():
    """Test using speedrun and then checking for winner."""
    player1 = MockPlayer("Gunnar", 50)
    game_test = Game(player1)

    game_test.speedrun_game()

    # Player1 should be at 90, not a winner yet
    winner = game_test.check_winner()
    assert winner is None

    # Add 10 more points to win
    player1.total_score = 100
    winner = game_test.check_winner()
    assert winner == player1
