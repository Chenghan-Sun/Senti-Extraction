import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize

class StaA(object):
    '''will figure out how to add "self" later
    '''
    def filter_out(data_path):
        selected_text=pd.read_csv(data_path)
        selected_text=selected_text['selected_text'].apply(str)
        split_selected_text=[]
        split_selected_word=[]
        for i in range(len(selected_text)):
            split_selected_text.append(word_tokenize(selected_text[i]))
            for j in split_selected_text[i]:
                split_selected_word.append(j)
        return split_selected_text, split_selected_word
        
        
        
        
    def nGram(split_selected_word, split_selected_text, N):
        if N == 1:
            print('Unigram text framework')
            # remove duplicate words
            unigram = list(set(split_selected_word))
            unigram_frequency = []
            unigram_presence = np.zeros(len(unigram))
            # count the frequency
            for o in range(len(unigram)):
                unigram_frequency.append(split_selected_word.count(unigram[o]))
                # count the times of presence
                for l in range(len(split_selected_text)):
                    if unigram[o] in split_selected_text[l]:
                        unigram_presence[o] += 1
            ngram = unigram
            n_gram=unigram
            ngram_presence = unigram_presence
            ngram_frequency = unigram_frequency
        else:
            print(f"{N}-gram text frame work")
            n_gram=[]
            ngram = []
            # classify the data by N words in one unit
            for k in range(len(split_selected_text)):
                n_gram.append([])
                for m in range(0, len(split_selected_text[k]) - (N - 1)):
                    string = split_selected_text[k][m]
                    for g in range(1, N):
                        string = string + " " + split_selected_text[k][m + g]
                    ngram.append(str(string))
                    n_gram[k].append(str(string))
            gram = list(set(ngram))
            ngram_frequency = []
            ngram_presence = np.zeros(len(gram))
            # count the frequency
            for o in range(len(gram)):
                ngram_frequency.append(ngram.count(gram[o]))
                for l in range(len(n_gram)):
                    if ngram[o] in n_gram[l]:
                        ngram_presence[o] += 1
            ngram=gram
        number_unique_term = len(ngram)

        return ngram, ngram_presence, ngram_frequency, number_unique_term,n_gram
        
    
    def ranking(ngram_frequency,ngram_presence,ngram, path_rank):
        frame=pd.DataFrame({'frequency':ngram_frequency,'presence':ngram_presence},index=ngram)
        rank=frame.sort_values(by=['frequency'],ascending=False)
        frequency_ranking=rank['frequency']
        presence_ranking=rank['presence']
        rank.to_csv(path_rank)
        
        return frequency_ranking,presence_ranking,rank
