"""Module that prints dictionary pretty"""


class HighScore:
    """Dictionary containing  playerID:Player"""

    _chart = {}

    def __init__(self, chart):
        self.chart = chart

    def sort_dict(input_dict):
        """sort dictionary in descending order <br>
        p.s.: pylint says that i should add self for this method, but I strongly disagree
        """
        return (
            dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=True))
            if isinstance(input_dict, dict)
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
        scores = HighScore.sort_dict(self.chart)
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
