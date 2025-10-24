class MockPlayer:
    def __init__(self, username, total_score):
        self.__username = username
        self.total_score = total_score

    def change_usr_name(self, new_username):
        if new_username is not None:
            self.__username = new_username

    def set_total_score(self, new_total_score):
        if new_total_score is not None:
            self.total_score = new_total_score

    def get_username(self):
        return self.__username

    def get_total_score(self):
        return self.total_score