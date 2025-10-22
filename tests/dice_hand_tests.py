"""Unit Test Module for DiceHand."""
import pytest
from program.dice_hand import DiceHand


def test_init_game_rolls_is_list_value():
    """test if game rolls is a list"""
    test_dicehand = DiceHand()
    assert isinstance(test_dicehand.game_rolls, list)
    #type(test_dicehand.game_rolls) == list


def test_init_turn_rolls_is_list_value():
    """test if turn rolls is a list"""
    test_dicehand = DiceHand()
    assert isinstance(test_dicehand.turn_rolls, list)


def test_init_type():
    """Test that DiceHand() creates an instance of DiceHand."""
    test_dicehand = DiceHand()
    assert type(test_dicehand) == type(DiceHand())


def test_add_turn_roll_remove_rolls_from_turnroll():
    """Test that add_turn_rolls() clears the turn_rolls list after adding."""
    test_dicehand = DiceHand()
    test_rolls = [3, 5, 3, 5, 2, 6]
    for i in test_rolls:
        test_dicehand.add_roll(i)
    test_dicehand.add_turn_rolls()
    assert not test_dicehand.turn_rolls


def test_add_turn_roll_moved_to_gamerolls():
    """Test that add_turn_rolls() moves turn_rolls content into game_rolls."""
    test_dicehand = DiceHand()
    test_rolls = [3, 5, 3, 5, 2, 6]
    for i in test_rolls:
        test_dicehand.add_roll(i)
    test_dicehand.add_turn_rolls()
    assert test_dicehand.game_rolls == test_rolls


def test_add_roll_is_added():
    """Test that add_roll() successfully adds a roll to turn_rolls."""
    test_dicehand = DiceHand()
    test_dicehand.add_roll(6)
    assert test_dicehand.turn_rolls[0] == 6


def test_add_roll_is_less_6():
    """Test that added roll values are within the valid dice range (1–6)."""
    test_dicehand = DiceHand()
    test_dicehand.add_roll(9)
    assert not test_dicehand.turn_rolls
    # test_dicehand.turn_rolls[0] >= 1 and test_dicehand.turn_rolls[0] <= 6


def test_add_roll_is_more_than_1():
    """Test that added roll values are within the valid dice range (1–6)."""
    test_dicehand = DiceHand()
    test_dicehand.add_roll(0)
    assert not test_dicehand.turn_rolls
    # test_dicehand.turn_rolls[0] >= 1 and test_dicehand.turn_rolls[0] <= 6)


def test_add_roll_None_value():
    """Test that add_roll(None) raises a TypeError."""
    with pytest.raises(
        TypeError
    ):  # didn't work with match, so i gave up; you can rewrite it ofc
        test_dicehand = DiceHand()
        test_dicehand.add_roll(None)


def test_add_roll_list_value():
    """Test that add_roll(None) raises a TypeError."""
    with pytest.raises(
        TypeError
    ):  # didn't work with match, so i gave up; you can rewrite it ofc
        test_dicehand = DiceHand()
        test_dicehand.add_roll([1, 2, 4, 7])


def test_sum_game_rolls():
    """Test that sum_game_rolls() returns the correct total of all game rolls."""
    test_dicehand = DiceHand()
    test_rolls = [1, 3, 5, 3, 6, 2, 5, 2, 4]
    for i in test_rolls:
        test_dicehand.add_roll(i)
    test_dicehand.add_turn_rolls()
    exp_sum = 31
    assert test_dicehand.sum_game_rolls() == exp_sum


def test_sum_game_rolls_with_non_int_value():
    """Test that sum_game_rolls() ignores non-integer values when summing."""
    test_dicehand = DiceHand()
    test_rolls = [1, 3, 5, 3, 6, "", 5, 2, 4]
    for i in test_rolls:
        test_dicehand.add_roll(i)
    test_dicehand.add_turn_rolls()
    exp_sum = 29  # 31
    assert test_dicehand.sum_game_rolls() == exp_sum


def test_sum_turn_rolls_with_1_to_5_dice(monkeypatch):
    """Test that sum_turn_rolls() correctly sums 1–5 integer dice values."""
    test_dicehand = DiceHand()
    for i in range(1, 6):
        # 1,2,3,4,5
        test_dicehand.add_roll(i)
    expected_sum = 15
    actual_sum = test_dicehand.sum_turn_rolls()
    assert actual_sum == expected_sum, f"Expected {expected_sum}, got {actual_sum}"


def test_sum_turn_rolls_with_non_int_value(monkeypatch):
    """Test that sum_turn_rolls() ignores non-integer values in the roll list."""
    test_dicehand = DiceHand()
    test_rolls = [1, 5, 4, 2, 6, "hihi"]
    for i in test_rolls:
        test_dicehand.add_roll(i)
    expected_sum = 20
    actual_sum = test_dicehand.sum_turn_rolls()
    assert actual_sum == expected_sum


def test_sum_turn_rolls_with_5_dice_value_4(monkeypatch):
    """Test that sum_turn_rolls() correctly sums five dice all showing 4."""
    test_dicehand = DiceHand()
    for i in range(1, 6):
        test_dicehand.add_roll(4)
    expected_sum = 20
    actual_sum = test_dicehand.sum_turn_rolls()
    assert actual_sum == expected_sum, f"Expected {expected_sum}, got {actual_sum}"
