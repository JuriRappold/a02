from dice import Dice
#from dice_hand import DiceHand

class Player:
    _next_id = 0

    def __init__(self,name):
        if isinstance(name,str) and name != '':
            self.__username = name
            self.__player_id = Player._next_id
            # self._diceHand = DiceHand()
            self.__total_score = 0
            print(Player._next_id)
            Player._next_id += 1
        else: raise TypeError("name should be string!")

    def roll_dice(self):
        dice = Dice.roll_dice()
        #self._diceHand.append(dice)
        return dice

    def change_username(self,new_name):
        if isinstance(new_name,str) and new_name != '':
            self.__username = new_name
        else: raise TypeError("name should be string!")

    def get_username(self):
        return self._username

    def get_total_score(self):
        return self._total_score

    # for cheating purposes?
    def set_total_score(self, score):
        self.total_score = score
        pass

    def set_dice_hand(dice_hand_list):
        # self.diceHand = dice_hand_list
        pass
