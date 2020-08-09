import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize


class StaA(object):
    """will figure out how to add "self" later
    """

    def __init__(self, data_path):
        self.data_path = data_path
        self.n_document = 0
        self.n_gram = []
        self.ngram = []
        self.ngram_frequency = []
        self.ngram_presence = []
        self.number_unique_term = None
        self.split_selected_text = None
        self.split_selected_word = None
        self.N = None
        self.rank = None
        self.idf_ranking = None
        self.tf_idf_ranking = None
        self.frequency_ranking = None
        self.presence_ranking = None

    def filter_out(self):
        selected_text = pd.read_csv(self.data_path)
        selected_text = selected_text['selected_text'].apply(str)
        self.n_document = len(selected_text)
        self.split_selected_text = []
        self.split_selected_word = []
        for i in range(len(selected_text)):
            self.split_selected_text.append(word_tokenize(selected_text[i]))
            for j in self.split_selected_text[i]:
                self.split_selected_word.append(j)
        return self.split_selected_text, self.split_selected_word, self.n_document

    def nGram(self, N):
        self.N = N
        if not self.split_selected_text or not self.split_selected_word:
            raise Exception("Use filter_out function to filter the data at first")
        print(f"{self.N}-gram text frame work")
        self.n_gram = []
        self.ngram = []
        # classify the data by N words in one unit
        for k in range(len(self.split_selected_text)):
            self.n_gram.append([])
            for m in range(0, len(self.split_selected_text[k]) - (self.N - 1)):
                string = self.split_selected_text[k][m]
                for g in range(1, N):
                    string += " " + self.split_selected_text[k][m + g]
                self.ngram.append(str(string))
                self.n_gram[k].append(str(string))
        gram = list(set(self.ngram))
        self.ngram_frequency = []
        self.ngram_presence = np.zeros(len(gram))
        # count the frequency
        for i in range(len(gram)):
            self.ngram_frequency.append(self.ngram.count(gram[i]))
            for j in range(len(self.n_gram)):
                if self.ngram[i] in self.n_gram[j]:
                    self.ngram_presence[i] += 1
        self.ngram = gram
        self.number_unique_term = len(self.ngram)

        return self.ngram, self.ngram_presence, self.ngram_frequency, self.number_unique_term, self.n_gram

    def ranking(self, path_rank):
        if not self.ngram:
            raise Exception("Clarify the number of N by method nGram")
        idf = []
        tf_idf = []
        for i in range(len(self.ngram)):
            idf.append(np.log((1 + self.n_document) / (1 + self.ngram_presence[i])) + 1)
            tf_idf.append(self.ngram_frequency[i] * idf[i])
        frame = pd.DataFrame({'frequency': self.ngram_frequency,
                              'presence': self.ngram_presence,
                              'idf': idf, 'tf-idf': tf_idf},
                             index=self.ngram)
        self.rank = frame.sort_values(by=['frequency'], ascending=False)
        self.idf_ranking = self.rank['idf']
        self.tf_idf_ranking = self.rank['tf-idf']
        self.frequency_ranking = self.rank['frequency']
        self.presence_ranking = self.rank['presence']
        self.rank.to_csv(path_rank)

        return self.frequency_ranking, self.presence_ranking, self.idf_ranking, self.tf_idf_ranking, self.rank

    def plot_ranking(self, head_number=50):
        if not self.frequency_ranking:
            raise Exception("Use ranking function to get the rank first")
        plt.subplot(4, 1, 1)
        self.frequency_ranking.head(head_number).plot.bar(figsize=(15, 10))
        plt.title('Appearing_Time')
        plt.subplot(4, 1, 2)
        self.presence_ranking.head(head_number).plot.bar(figsize=(15, 10))
        plt.title('Appearing_Document')
        plt.subplot(4, 1, 3)
        self.idf_ranking.head(head_number).plot.bar(figsize=(15, 10))
        plt.title('idf')
        plt.subplot(4, 1, 4)
        self.tf_idf_ranking.head(head_number).plot.bar(figsize=(15, 10))
        plt.title('tf-idf')
