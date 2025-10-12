class HighScore:
    '''Dictionary containing  playerID:Player'''
    _chart = {1:23,
             2:15} 

    def __init__(self, chart):
        #on later stage of development, implement this as functional method, where it stores PlayerID and PLayer every time when it's called
        self.chart = chart

    def get_chart(self):
        # sort dictionary in descending order
        scores = dict(sorted(self.chart.items(), key=lambda item: item[1], reverse=True))
        #dict -> convert tuples into dictionary back
        # sorted() -> sort those tuples using a specific rule  
        #self.chart.items() -> get dictionary as tuples
        #key=lambda item -> iterate through each item
        #item[1] -> iterate through item value
        #reverse=True -> do it in descending, not ascending order
        
        table = '''
        ╔════════════════════════════╗
        ║       🏅 LEADERBOARD       ║
        ╠════════════════════════════╣
        '''

        lines = map(lambda score: f"║ {score[0]:>2}. {score[1][0]:<14} │ {score[1][1]:>5} ║\n        ", enumerate(scores.items(), 1))
        
        for line in lines:
            table += line

        table += '╚════════════════════════════╝'


        print(table)
        return table
    
if __name__ == "__main__":
    scores = HighScore({1:28, 2:19})
    scores.get_chart()
