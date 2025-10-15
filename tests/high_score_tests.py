from program.high_score import HighScore
import pytest


def test_get_chart_returns_string():
    """Test that get_chart returns a string"""
    scores = HighScore({"Rob": 28, "Moth": 19})
    res = scores.get_chart()
    assert isinstance(res, str)

def test_get_chart_input_non_dictionary():
    """Test that get_chart detects non-dictionary value"""
    scores = HighScore('heheeee >:]')
    res = scores.get_chart()
    exp = "Wrong value/empty dictionary, unable generate table"
    assert exp == res


def test_get_chart_input_empty_dictionary():
    """Test that get_chart detects empty dictionary"""
    scores = HighScore({})
    res = scores.get_chart()
    exp = "Wrong value/empty dictionary, unable generate table"
    assert exp == res


def test_get_chart_input_small_dictionary():
    """Test that get_chart contains proper values"""
    test_dict = {"Rob": 28, "Moth": 19}
    scores = HighScore(test_dict).get_chart()
    #CHECKS ONLY FOR NAMES, NOT VALUES
    exp = list(test_dict)
    print(exp)
    for word in exp:
        assert word in scores


def test_get_chart_input_big_dictionary():
    """Test that get_chart returns multiple players"""
    test_dict = {"Rob": 28, "Moth": 19, "RuX":56, "Yuwch":98}
    scores = HighScore(test_dict).get_chart()
    print(scores)
    exp = list(test_dict)
    for word in exp:
        assert word in scores


def test_sort_dict_input_unsorted():
    """Test that sort_chart sorts properly"""
    test_dict ={1:15, 4:19, 2:18}
    res = HighScore.sort_dict(test_dict)
    exp = {1: 15, 2: 18, 4: 19}
    assert res == exp

def test_sort_dict_input_int():
    """Test that sort_chart can handle int"""
    res = HighScore.sort_dict(5)
    exp = {}
    assert res == exp


def test_sort_dict_input_None():
    """Test that sort_chart can handle None"""
    res = HighScore.sort_dict(5)
    exp = {}
    assert res == exp


def test_sort_dict_input_list():
    """Test that sort_chart can handle list"""
    res = HighScore.sort_dict([15,14,124,3456,567,'apple','ado'])
    exp = {}
    assert res == exp

def test_sort_dict_input_tuple():
    """Test that sort_chart can handle tuple"""
    res = HighScore.sort_dict((1,4,3,'f'))
    exp = {}
    assert res == exp
