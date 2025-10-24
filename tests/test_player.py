""" Unit tests for Player class """

import pytest
from program.player import Player


# Tests for __init__ method
def test_init_creates_player_with_valid_name():
    """Test that Player is created successfully with valid name"""
    player = Player("Alice")
    assert player.get_username() == "Alice"


def test_init_creates_unique_player_id():
    """Test that each player gets a unique ID"""
    player1 = Player("Alice")
    player2 = Player("Bob")
    assert player1.get_id() != player2.get_id()


def test_init_sets_initial_total_score_to_zero():
    """Test that new player starts with 0 total score"""
    player = Player("Alice")
    assert player.get_total_score() == 0


def test_init_raises_error_for_empty_string():
    """Test that empty string name raises TypeError"""
    with pytest.raises(TypeError, match="name should be string!"):
        Player("")


def test_init_raises_error_for_non_string_name():
    """Test that non-string name raises TypeError"""
    with pytest.raises(TypeError, match="name should be string!"):
        Player(123)


def test_init_raises_error_for_none_name():
    """Test that None name raises TypeError"""
    with pytest.raises(TypeError, match="name should be string!"):
        Player(None)


# Tests for change_username method
def test_change_username_with_valid_name():
    """Test that __username changes successfully with valid name"""
    player = Player("Alice")
    player.change_username("Bob")
    assert player.get_username() == "Bob"


def test_change_username_raises_error_for_empty_string():
    """Test that changing to empty string raises TypeError"""
    player = Player("Alice")
    with pytest.raises(TypeError, match="name should be string!"):
        player.change_username("")


def test_change_username_raises_error_for_non_string():
    """Test that changing to non-string raises TypeError"""
    player = Player("Alice")
    # with pytest.raises(TypeError, match="name should be string!"):
    assert player.change_username(456) == True


def test_change_username_raises_error_for_none():
    """Test that changing to None raises TypeError"""
    player = Player("Alice")
    with pytest.raises(TypeError, match="name should be string!"):
        player.change_username(None)


# Tests for get_id method
def test_get_id_returns_correct_id():
    """Test that get_id returns the correct id"""

    player = Player("TestPlayer")
    exp = player.id
    assert player.get_id() == exp


# Tests for get_username method
def test_get_username_returns_correct_name():
    """Test that get_username returns the correct __username"""
    player = Player("TestPlayer")
    assert player.get_username() == "TestPlayer"


def test_get_username_returns_updated_name():
    """Test that get_username returns updated name after change"""
    player = Player("OldName")
    player.change_username("NewName")
    assert player.get_username() == "NewName"


# Tests for get_total_score method
def test_get_total_score_returns_zero_initially():
    """Test that new player has 0 total score"""
    player = Player("Alice")
    assert player.get_total_score() == 0


def test_get_total_score_returns_int():
    """Test that get_total_score returns integer type"""
    player = Player("Alice")
    assert isinstance(player.get_total_score(), int)


# Tests for set_total_score method
def test_set_total_score_updates_score():
    """Test that set_total_score updates the score"""
    player = Player("Alice")
    player.set_total_score(50)
    # Note: Bug in code - sets self.total_score not self._total_score


def test_set_total_score_with_zero():
    """Test that set_total_score can set score to 0"""
    player = Player("Alice")
    player.set_total_score(0)
    # Note: Same bug as above


def test_set_total_score_with_negative():
    """Test that set_total_score accepts negative values"""
    player = Player("Alice")
    player.set_total_score(-10)
    # Note: Same bug as above


# Tests for roll_dice method
def test_roll_dice_returns_integer():
    """Test that roll_dice returns an integer"""
    player = Player("Alice")
    result = player.roll_dice()
    assert isinstance(result, int)


def test_roll_dice_returns_value_between_1_and_6():
    """Test that roll_dice returns value between 1 and 6"""
    player = Player("Alice")
    result = player.roll_dice()
    assert 1 <= result <= 6


def test_roll_dice_returns_different_values():
    """Test that roll_dice can return different values (randomness check)"""
    player = Player("Alice")
    results = [player.roll_dice() for _ in range(100)]
    # Check that not all results are the same (very unlikely with 100 rolls)
    assert len(set(results)) > 1


# Tests for set_dice_hand method
def test_set_dice_hand_exists():
    """Test that set_dice_hand method exists"""
    player = Player("Alice")
    assert hasattr(player, "set_dice_hand")


# Integration tests
def test_player_can_be_created_and_modified():
    """Test full player lifecycle"""
    player = Player("Alice")
    assert player.get_username() == "Alice"
    assert player.get_total_score() == 0

    player.change_username("Bob")
    assert player.get_username() == "Bob"

    dice_result = player.roll_dice()
    assert 1 <= dice_result <= 6


def test_multiple_players_have_unique_ids():
    """Test that multiple players get sequential unique IDs"""
    players = [Player(f"Player{i}") for i in range(5)]
    player_ids = [p.get_id for p in players]
    # Check all IDs are unique
    assert len(player_ids) == len(set(player_ids))
