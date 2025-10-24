"""Tests for class high_score.py"""

import pytest

from program.high_score import HighScore
from program.player import Player
from tests.mock_player import MockPlayer


def test_init_creates_instance():
    """Test that __init__ creates a HighScore instance with chart"""
    test_chart = {"Rob": 28, "Moth": 19}
    rob = Player("Rob")
    moth = Player("Moth")
    rob.set_total_score(28)
    moth.set_total_score(19)
    scores = HighScore(rob, moth)
    assert scores.chart == test_chart
    assert isinstance(scores, HighScore)


def test_get_chart_returns_string():
    """Test that get_chart returns a string"""
    rob = Player("Rob")
    moth = Player("Moth")
    rob.set_total_score(28)
    moth.set_total_score(19)
    scores = HighScore(rob, moth)
    res = scores.get_chart()
    assert isinstance(res, str)


def test_get_chart_input_non_dictionary():
    """Test that get_chart detects non-dictionary value"""
    with pytest.raises(TypeError, match="Not a Player or Computer"):
        HighScore("heheeee >:]", 3.20)


def test_get_chart_input_none_parameters():
    """Test that get_chart detects empty dictionary"""
    with pytest.raises(TypeError, match="NoneType not allowed"):
        HighScore(None, None)
    # res = scores.get_chart()
    # exp = "Wrong value/empty dictionary, unable generate table"
    # assert exp == res


def test_get_chart_input_small_dictionary():
    """Test that get_chart contains proper values"""
    test_dict = {"Rob": 28, "Moth": 19}
    rob = Player("Rob")
    moth = Player("Moth")
    rob.set_total_score(28)
    moth.set_total_score(19)
    scores = HighScore(rob, moth).get_chart()
    # CHECKS ONLY FOR NAMES, NOT VALUES
    exp = list(test_dict)
    print(exp)
    for word in exp:
        assert word in scores


# def test_get_chart_input_big_dictionary():
#     """Test that get_chart returns multiple players"""
#     test_dict = {"Rob": 28, "Moth": 19, "RuX": 56, "Yuwch": 98}
#     rob = Player("Rob")
#     moth = Player("Moth")
#     rob.set_total_score(28)
#     moth.set_total_score(19)
#     rux = Player("RuX")
#     rux.set_total_score(56)
#     yuwch = Player("Yuwch")
#     yuwch.set_total_score()
#
#     scores = HighScore(test_dict).get_chart()
#     print(scores)
#     exp = list(test_dict)
#     for word in exp:
#         assert word in scores


def test_get_chart_contains_leaderboard_header():
    """Test that get_chart includes LEADERBOARD header"""
    alice = Player("Alice")
    alice.set_total_score(50)
    bob = Player("Bob")
    bob.set_total_score(24)
    scores = HighScore(alice, bob)
    res = scores.get_chart()
    assert "LEADERBOARD" in res


def test_get_chart_formats_correctly():
    """Test that get_chart contains proper formatting characters"""
    alice = Player("Alice")
    alice.set_total_score(50)
    bob = Player("Bob")
    bob.set_total_score(24)
    # alice = MockPlayer("Alice", 50)
    # bob = MockPlayer("Bob", 24)
    scores = HighScore(alice, bob)
    res = scores.get_chart()
    assert "║" in res
    assert "╔" in res or "=" in res
