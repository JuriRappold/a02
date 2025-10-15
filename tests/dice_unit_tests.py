"""unit tests for dice.py"""
import pytest
from program.dice import Dice


def test_non_int0():
    """non-integer parameter test --> parameter is a string."""
    with pytest.raises(TypeError, match="Roll is not an integer!"):
        # non-int inputs
        Dice.get_dice_face("hello")


def test_non_int1():
    """non-integer parameter test --> parameter is a float"""
    with pytest.raises(TypeError, match="Roll is not an integer!"):
        Dice.get_dice_face(3.20)


def test_non_int2():
    """non-integer parameter test --> parameter is an Array."""
    with pytest.raises(TypeError, match="Roll is not an integer!"):
        Dice.get_dice_face([1, 2.2, "h"])


def test_dice_face0():
    """index-out-of-bounds parameter test --> parameter is 0."""
    with pytest.raises(IndexError, match="Roll out of Bounds"):
        # int inputs
        Dice.get_dice_face(0)


def test_dice_face1():
    """index-out-of-bounds parameter test --> parameter is negative."""
    with pytest.raises(IndexError, match="Roll out of Bounds"):
        Dice.get_dice_face(-5)


def test_dice_face2():
    """index-out-of-bounds parameter test --> parameter is positive & higher than 6."""
    with pytest.raises(IndexError, match="Roll out of Bounds"):
        Dice.get_dice_face(100)


def test_pos_input():
    """positive test that makes sure if a valid value is inputted, the correct value is returned."""
    # positive test
    assert Dice.get_dice_face(3) == "3"
