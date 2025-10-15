class HighScore:
    """Dictionary containing  playerID:Player"""

    _chart = {}

    def __init__(self, chart):
        # on later stage of development, implement this as functional method, where it stores PlayerID and PLayer every time when it's called
        self.chart = chart

    def sort_dict(input_dict):
        """sort dictionary in descending order"""
        return (
            dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=True))
            if type(input_dict) == dict
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
        if type(scores) != dict or scores == dict(): return "Wrong value/empty dictionary, unable generate table"
        score_lines = "".join(
            map(
                lambda score: f"║ {score[0]:>2}. {score[1][0]:<14} │ {score[1][1]:>5} ║\n        ",
                enumerate(scores.items(), 1),
            )
        )
        # "".join ->append to table lines that lambda generated
        # score: / enumerate(scores.items(), 1))) -> score is enumerate(scores.items(), 1)))
        # f"║ {score[0]:>2}. {score[1][0]:<14} │ {score[1][1]:>5} ║\n        ", -> fstring which makes it pretty
        # umerate(scores.items(), 1))) -> creates dictionary with dictionary in it [rank[name,score]]

        # join generated lines into table
        table = f"""
        ╔════════════════════════════╗
        ║       🏅 LEADERBOARD       ║
        ╠════════════════════════════╣
        {score_lines}╚════════════════════════════╝"""
        return table

'''
if __name__ == "__main__":
    scores = HighScore({"Rob": 28, "Moth": 19})
    print(scores.get_chart())'''
