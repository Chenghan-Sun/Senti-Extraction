import pandas as pd
import numpy as np
from typing import List, Tuple


class BaseLine:
    def __init__(self, dataFrame: pd.DataFrame, **corpus: List[str]) -> None:
        self.positive_corpus = self.corpus_to_set(corpus.pop('positive_corpus'))
        self.negative_corpus = self.corpus_to_set(corpus.pop('negative_corpus'))
        self.data = dataFrame.copy()

    def sentiment_count(self, featureName='text'):
        self.data[['(positive, negative)']] = self.data[featureName].apply(self.text_sentiment_count())

    def text_sentiment_count(self, textLine: str) -> Tuple[int, int]:
        pos = 0
        neg = 0
        for word in textLine.split():
            if word in self.positive_corpus:
                pos += 1
            elif word in self.negative_corpus:
                neg += 1

        return pos, neg

    @staticmethod
    def corpus_to_set(corpus):
        words = set()
        with open(corpus, 'r') as lines:
            for line in lines:
                words.add(line.strip())
        return words
