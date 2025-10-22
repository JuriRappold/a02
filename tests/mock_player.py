class MockPlayer:
    def __init__(self, username, total_score):
        self.username = username
        self.total_score = total_score

    def change_usr_name(self, new_username):
        if new_username is not None:
            self.username = new_username

    def set_total_score(self, new_total_score):
        if new_total_score is not None:
            self.total_score = new_total_score
