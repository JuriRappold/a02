"""
dice modul, see class description for function
"""

import random

class Dice:
    '''
    static Dice class, only really need the roll dice method;
    could be a static class? --> "easiest" way would just be a python file with functions
    done it the "Java" way, source:
    https://stackoverflow.com/questions/30556857/creating-a-static-class-with-no-instances
    '''
    # Attributes
    # static class wide variable, "real" dice faces will be added later
    # DO NOT CHANGE LENGTH!! Only change to get new dice faces
    __STRING_DICE_FACE = ["1", "2", "3", "4", "5", "6"]

    # Methods
    @staticmethod
    def roll_dice():
        """
        :return: random integer between 1 and 6 (inclusive of both ends)
        """
        return random.randint(1,6)


    @staticmethod
    def get_dice_face(roll):
        """
        :param roll: an integer between 1 and 6 (inclusive);
        raises either TypeError(roll is not an integer) or
        an IndexError(not between 1 and 6 inclusive)
        :return: corresponding dice face is returned
        """
        if isinstance(roll, int):
            if 0 < roll < 7:
                return Dice.__STRING_DICE_FACE[roll-1]
            raise IndexError("Roll out of Bounds")
        raise TypeError("Roll is not an integer!")
