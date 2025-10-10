class Computer:
    def __init__(self, computer_name, difficulty):
        self.computer_name = computer_name
        self.difficulty = difficulty
        self.id = hash(computer_name+difficulty)


    def select_difficulty(self, new_difficulty):
        pass

    def change_computer_name(self, new_name):
        pass
