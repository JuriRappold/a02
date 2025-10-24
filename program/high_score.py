"""Module that prints dictionary pretty"""
from program.computer import Computer
from program.player import Player
from tests.mock_player import MockPlayer


class HighScore:
    """Dictionary containing  playerID:Player"""

    _chart = {}

    def __init__(self, player1, opponent):
        if player1 and opponent:
            if isinstance(player1, Player | MockPlayer) and isinstance(opponent, Player | Computer | MockPlayer):
                self.chart = {player1.get_username() : player1.get_total_score(), opponent.get_username() : opponent.get_total_score() }
            else: raise TypeError("Not a Player or Computer" )#: player1: {type(player1)}; opponent: {type(opponent)}
        else: raise TypeError("NoneType not allowed")

    def sort_dict(self):
        """sort dictionary in descending order <br>
        p.s.: pylint says that i should add self for this method, but I strongly disagree
        """
        return (
            dict(sorted(self.chart.items(), key=lambda item: item[1], reverse=True))
            if isinstance(self.chart, dict)
            else {}
        )
        # dict -> convert tuples into dictionary back
        # sorted() -> sort those tuples using a specific rule
        # self.chart.items() -> get dictionary as tuples
        # key=lambda item -> iterate through each item
        # item[1] -> iterate through item value
        # reverse=True -> do it in descending, not ascending order

    def get_chart(self):
        """generate nice table player-score"""
        scores = HighScore.sort_dict(self)
        if not isinstance(scores, dict) or not scores:
            return "Wrong value/empty dictionary, unable generate table"
        score_lines = "".join(
            map(
                lambda score: f"║ {score[0]:>2}. {score[1][0]:<14} │ {score[1][1]:>5} ║\n        ",
                enumerate(scores.items(), 1),
            )
        )
        # "".join ->append to table lines that lambda generated
        # score: / enumerate(scores.items(), 1)))
        #       -> score is enumerate(scores.items(), 1)))
        # f"║ {score[0]:>2}. {score[1][0]:<14} │ {score[1][1]:>5} ║\n",
        #       -> fstring which makes it pretty
        # umerate(scores.items(), 1)))
        #       -> creates dict with dict in it [rank[name,score]]

        # join generated lines into table
        table = f"""
        ╔════════════════════════════╗
        ║       🏅 LEADERBOARD       ║
        ╠════════════════════════════╣
        {score_lines}╚════════════════════════════╝"""
        return table
