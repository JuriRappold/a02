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

        #make sorted list pretty 
        table += "".join(map(lambda score: f"║ {score[0]:>2}. {score[1][0]:<14} │ {score[1][1]:>5} ║\n        ", enumerate(scores.items(), 1)))
        # "".join ->append to table lines that lambda generated
        # score: / enumerate(scores.items(), 1))) -> score is enumerate(scores.items(), 1)))
        # f"║ {score[0]:>2}. {score[1][0]:<14} │ {score[1][1]:>5} ║\n        ", -> fstring which makes it pretty
        # umerate(scores.items(), 1))) -> creates dictionary with dictionary in it [rank[name,score]] 

        

        table += '╚════════════════════════════╝'


        print(table)
        return table
    
if __name__ == "__main__":
    scores = HighScore({"Minmi":28, "RuX":19})
    scores.get_chart()
