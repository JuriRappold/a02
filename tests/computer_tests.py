from program.computer import Computer
from program.dice import Dice
import pytest

#TEST INIT
def test_init_values():
    '''test those: computer_name = computer_name
        self.difficulty = difficulty  # has to be a tuple
        self.id = hash(computer_name + difficulty)
        self.dice_hand = DiceHand()  # create dice_hand obj once class is integrated
        self.score = 0
        self.turn_number = 0  '''
    assert True

def test_init_class():
    '''Test that it initialises right'''
    test_pc = Computer('Nephilim', 'easy')
    assert type(test_pc) == Computer 

def test_init_same_name_value():
    '''check that input name value are actually stored inside'''
    name_exp = 'Nephilim'
    test_pc = Computer(name_exp, 'easy')
    assert  test_pc.computer_name == name_exp 

def test_init_values_empty_value_computer_name():
    test_pc = Computer('', 'easy')
    assert test_pc.computer_name != ''

def test_init_values_None_value_computer_name():
    test_pc = Computer(None, 'easy')
    assert type(test_pc.computer_name) == str

def test_init_values_dict_value_computer_name():
    test_pc = Computer({4:5,8:2}, 'easy')
    assert type(test_pc.computer_name) == str

def test_init_values_list_value_computer_name():
    test_pc = Computer([4,7,9], 'easy')
    assert type(test_pc.computer_name) == str

def test_init_values_list_value_difficulty():
    test_pc = Computer('Nephilim', 'easy')
    assert type(test_pc.computer_name) == str

def test_init_same_difficulty_value():
    '''check that input difficulty value are actually stored inside'''
    exp = ('easy', 1)
    test_pc = Computer('Clayman', exp)
    assert test_pc.difficulty == exp    

def test_init_difficulty_is_tuple():
    '''check that difficulty is a tuple'''
    difficulty = ('easy',1)
    test_pc = Computer('Clayman', difficulty)
    assert  type(test_pc.difficulty) == tuple 

def test_init_difficulty_dict_values():
    '''check that difficulty can handle Dict value'''
    difficulty = {4:5,6:2}
    test_pc = Computer('Clayman', difficulty)
    assert  type(test_pc.difficulty) != dict 

def test_init_difficulty_None_value():
    '''check that difficulty can handle None value'''
    difficulty = None
    test_pc = Computer('Clayman', difficulty)
    assert  type(test_pc.difficulty) != None 

def test_init_difficulty_str_value():
    '''check that difficulty can handle str value'''
    difficulty = ''
    test_pc = Computer('Clayman', difficulty)
    assert  type(test_pc.difficulty) != str 

#test that you can't change computer_name value?

def test_init_values():
    '''test those: computer_name = computer_name
        self.difficulty = difficulty  # has to be a tuple
        self.id = hash(computer_name + difficulty)
        self.dice_hand = DiceHand()  # create dice_hand obj once class is integrated
        self.score = 0
        self.turn_number = 0  '''
    assert True

def test_difficulty_values():
    assert True

#DIFFICULTY CHANGE
def test_select_difficulty_normal():
    test_pc = Computer('Nephilim', ('easy', 1))
    msg = test_pc.select_difficulty("normal")
    assert test_pc.difficulty == (2, "normal")
    assert msg == "Difficulty changed to: normal"


def test_select_difficulty_invalid():
    test_pc = Computer('Nephilim', ('easy', 1))
    msg = test_pc.select_difficulty("insane")
    assert "Invalid Difficulty Option" in msg
    assert test_pc.difficulty == ('easy', 1)


#TEST CHANGE COMPUTER NAME
def test_change_computer_name():
    test_pc = Computer('Name1', 'easy')
    exp = 'Nephilim'
    test_pc.change_computer_name(exp)
    assert test_pc.computer_name == exp

def test_change_name_same_id():
    test_pc = Computer('Name1', 'easy')
    first_id = test_pc.id
    test_pc.change_computer_name('Cool new name')
    second_id = test_pc.id
    assert first_id == second_id

def test_change_name_empty_value():
    first_name = 'Name1'
    empty_name = ''
    test_pc = Computer(first_name, 'easy')
    test_pc.change_computer_name(empty_name)
    assert test_pc.computer_name != empty_name

def test_change_name_dictionary_value():
    first_name = 'Name1'
    dict_name = {1:4,6:2}
    test_pc = Computer(first_name, 'easy')
    test_pc.change_computer_name(dict_name)
    print(test_pc.computer_name)
    assert type(test_pc.computer_name) == str

def test_change_name_list_value():
    first_name = 'Name1'
    list_name = [2,4,8,0]
    test_pc = Computer(first_name, 'easy')
    test_pc.change_computer_name(list_name)
    assert type(test_pc.computer_name) == str

def test_change_name_None_value():
    first_name = 'Name1'
    none_name = None
    test_pc = Computer(first_name, 'easy')
    test_pc.change_computer_name(none_name)
    assert type(test_pc.computer_name) == str

def test_roll_dice_type():
    test_pc = Computer('Nephilim', 'easy')
    test_dice = test_pc.roll_dice()
    assert type(test_dice) == int

def test_hold_at_twenty(monkeypatch):
    """force dice to always roll 5 -> stops after reaching >= 20"""
    test_pc = Computer('Nephilim', 'easy')
    monkeypatch.setattr('program.computer.Dice.roll_dice', lambda: 5)
    result = test_pc.hold_at_twenty()
    assert result == 20  # 5+5+5+5

def test_hold_at_twenty_roll_one(monkeypatch):
    rolls = iter([4, 1])  # roll 4, then 1
    monkeypatch.setattr('program.computer.Dice.roll_dice', lambda: next(rolls))
    test_pc = Computer('Nephilim', 'easy')
    result = test_pc.hold_at_twenty()
    assert result == 0  # resets after rolling 1

def test_take_turn_calls_correct():
    assert True

def test_scoring_turn():
    assert True

def test_keep_or_race():
    assert True

def test_take_turn():
    assert True

def test_():
    assert True

def test_():
    assert True

def test_():
    assert True

def test_():
    assert True

def test_():
    assert True

def test_():
    assert True

def test_():
    assert True

def test_():
    assert True

def test_():
    assert True
