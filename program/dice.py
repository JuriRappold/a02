import random

# Dice class, only really need the roll dice method;
# could be a static class? --> "easiest" way would just be a python file with functions
# done it the "Java" way, source: https://stackoverflow.com/questions/30556857/creating-a-static-class-with-no-instances
class Dice(object):
    # Attributes
    # static class wide variable, "real" dice faces will be added later
    # DO NOT CHANGE LENGTH!! Only change to get new dice faces
    STRING_DICE_FACE = ["1", "2", "3", "4", "5", "6"]

    # Methods
    @staticmethod
    def roll_dice():
        return random.randint(1,6)

    # how do I reference the constant STRING_DICE_FACE?
    # currently implemented as default value of a parameter, could be overwritten. --> see linting error
    @staticmethod
    def get_dice_face(roll, dice = STRING_DICE_FACE):
        if isinstance(roll, int) and 0< roll < 7: #type(roll) is int
            return dice[roll-1]
        raise Exception("Invalid roll entered; check parameter")

"""
pylinted this module, first "error" contains url
didn't have any docstrings yet; 

************* Module dice
contains url:
dice.py:5:0: C0301: Line too long (120/100) (line-too-long)
no clue what final newline is:
dice.py:26:0: C0304: Final newline missing (missing-final-newline)
DOCSTRINGS
dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dice.py:6:0: C0115: Missing class docstring (missing-class-docstring)
dice.py:16:4: C0116: Missing function or method docstring (missing-function-docstring)
dice.py:22:4: C0116: Missing function or method docstring (missing-function-docstring)

Indented "errors" were solved:
dice.py:6:0: R0205: Class 'Dice' inherits from object, can be safely removed from bases in python3 (useless-object-inheritance)

dice.py:22:4: W0102: Dangerous default value STRING_DICE_FACE (builtins.list) as argument (dangerous-default-value)

    dice.py:23:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)

    dice.py:23:11: C0123: Use isinstance() rather than type() for a typecheck. (unidiomatic-typecheck)

dice.py:26:12: W0719: Raising too general exception: Exception (broad-exception-raised)

-----------------------------------
Your code has been rated at 0.00/10

make: [Makefile:65: pylint] Error 28 (ignored)
"""
