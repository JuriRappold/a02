import dice

class Player:
    _next_id = 0
    #__username = ''
    #__player_id = 0
    #__total_score = 0
    # _diceHand = DiceHand()

    def __init__(self,name):
        self.__username = name
        self.__player_id = Player._next_id
        print(Player._next_id)
        Player._next_id += 1

    def roll_dice():
        #why this one is even on UML? it's dice, not player thing to do...
        #I understand save in dicehand, but not this
        pass

    def change_username(self,new_name):
        self.__username = new_name

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