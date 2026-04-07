import pandas as pd

class StatisticalAnalyzer:
    def __init__(self, character_list):
        if not character_list:
            self.df = pd.DataFrame()
        else:
            self.df = pd.DataFrame([c.to_dict() for c in character_list])

    def get_summary(self):
        if self.df.empty: return "No characters to analyze."
        # Returns mean, median (50%), max, and min for all numeric columns
        return self.df.describe().loc[['mean', '50%', 'max', 'min']]

    def save_to_csv(self, filename="data/characters.csv"):
        if not self.df.empty:
            self.df.to_csv(filename, index=False)
            return True
        return False
