import pytest
from program.menu import menu
from tests.mock_player import MockPlayer


# ----------- change_username(self, old_username, new_username) -------------------------------
def test_change_usrName_nulls():
    mockPlayer = MockPlayer("Mocker", 28)

    menuTest = menu()
    menuTest.set_player(mockPlayer)
    assert menuTest.change_username(None, None) == False

def test_change_usrName_oldNull():
    mockPlayer = MockPlayer("Mocker", 28)

    menuTest = menu()
    menuTest.set_player(mockPlayer)
    assert menuTest.change_username(None, "old Null") == False

def test_change_usrName_newNull():
    mockPlayer = MockPlayer("Mocker", 28)

    menuTest = menu()
    menuTest.set_player(mockPlayer)
    assert menuTest.change_username("Mocker", None) == False

def test_change_usrName_numbers():
    mockPlayer = MockPlayer("Mocker", 28)

    menuTest = menu()
    menuTest.set_player(mockPlayer)
    assert menuTest.change_username("Mocker", 2093) == True
def test_change_usrName_escapeChar():
    mockPlayer = MockPlayer("Mocker", 28)

    menuTest = menu()
    menuTest.set_player(mockPlayer)
    assert menuTest.change_username("Mocker", "Escape\nCharacter")==False

def test_change_usrName_player():
    mockPlayer = MockPlayer("Mocker", 28)

    menuTest = menu()
    menuTest.set_player(mockPlayer)
    assert menuTest.change_username(mockPlayer.username, MockPlayer("Username", 42)) == False
# still need some positive tests

# ----------- set_player(self, player) --------------------------------------------------------------
def test_set_player_None():
    menuTest = menu()

    assert menuTest.set_player(None) == False

def test_set_player_primitive():
    menuTest = menu()
    primitiveTypes = ["I'm a player!", 42, 3.20]
    for primitive in primitiveTypes:
        assert menuTest.set_player(primitive) == False

def test_set_player_list():
    menuTest = menu()
    primitiveTypes = ["I'm a player!", 42, 3.20]
    assert menuTest.set_player(primitiveTypes) == False

def test_set_player_player():
    menuTest = menu()
    mockPlayer = MockPlayer("Mocker", 28)

    assert menuTest.set_player(mockPlayer) == True


# ----------- validate_menu_choice(self, choice) --------------------------------------------------------------

def test_validate_menu_null():
    menuTest = menu()
    with pytest.raises(ValueError, match="False"):
        menuTest.validate_menu_choice(None)

def test_validate_menu_negNum():
    menuTest = menu()
    with pytest.raises(ValueError, match="False"):
        menuTest.validate_menu_choice(-3)

def test_validate_menu_float():
    menuTest = menu()
    with pytest.raises(ValueError, match="False"):
        menuTest.validate_menu_choice(3.14)

def test_validate_menu_string():
    menuTest = menu()
    with pytest.raises(ValueError, match="False"):
        menuTest.validate_menu_choice("Error incoming")

def test_validate_menu_player():
    menuTest = menu()
    mockPlayer = MockPlayer("Mocker", 28)
    with pytest.raises(ValueError, match="False"):
        menuTest.validate_menu_choice(mockPlayer)