import numpy as np


class StaA(object):

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
            gram = unigram
            presence = unigram_presence
            frequency = unigram_frequency
        else:
            print(f"{N}-gram text frame work")
            ngram = []
            # classify the data by N words in one unit
            for k in range(len(split_selected_text)):
                for m in range(0, len(split_selected_text[k]) - (N - 1)):
                    string = split_selected_text[k][m]
                    for g in range(1, N):
                        string = string + " " + split_selected_text[k][m + g]
                    ngram.append(str(string))
            gram = list(set(ngram))
            ngram_frequency = []
            ngram_presence = 'not applicable'
            # count the frequency
            for o in range(len(gram)):
                ngram_frequency.append(ngram.count(gram[o]))
            presence = ngram_presence
            frequency = ngram_frequency
        number_unique_term = len(gram)
        return gram, presence, frequency, number_unique_term
