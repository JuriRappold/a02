# import unittest
from program.dice import Dice
import pytest


def test_non_int0():
    with pytest.raises(TypeError, match="Roll is not an integer!"):
        # non-int inputs
        Dice.get_dice_face("hello")


def test_non_int1():
    with pytest.raises(TypeError, match="Roll is not an integer!"):
        Dice.get_dice_face(3.20)


def test_non_int2():
    with pytest.raises(TypeError, match="Roll is not an integer!"):
        Dice.get_dice_face([1, 2.2, "h"])


def test_dice_face0():
    with pytest.raises(IndexError, match="Roll out of Bounds"):
        # int inputs
        Dice.get_dice_face(0)


def test_dice_face1():
    with pytest.raises(IndexError, match="Roll out of Bounds"):
        Dice.get_dice_face(-5)


def test_dice_face2():
    with pytest.raises(IndexError, match="Roll out of Bounds"):
        Dice.get_dice_face(100)


def test_pos_input():
    # positive test
    assert Dice.get_dice_face(3) == "3"
