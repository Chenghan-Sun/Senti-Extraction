import pandas as pd


class SentiSeparation(object):
    def __init__(self, pd_df: pd.DataFrame) -> None:
        self.Pos=self.data[self.data['sentiment']=='positive']
        self.Neg=self.data[self.data['sentiment']=='negative']
        self.Neu=self.data[self.data['sentiment']=='neutral']
        self.Pos.to_csv(r'../data/Positive.csv')
        self.Neg.to_csv(r'../data/Negative.csv')
        self.Neu.to_csv(r'../data/Neutral.csv')