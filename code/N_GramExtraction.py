def nGram(split_selected_word,split_selected_text,N):
    
    """To separate typical texts into unigram,or multi-gram, and statistically analyze the texts.
input:
    split_selected_word: cleaned text to be analyzed. The unit of the variables should be a single word.
    split_selected_text: cleaned text to be analyzed. Each element contains a phrase or a sentence; however, the separated words of the phrase or the sentence are sub elements.
    N: number of words in one vector.
return: 
    gram:all the unique units of the analyzed data
    presence: how many times a unit appears in a phrase or a sentence: count 1 if exist in a phrase(sentence), 0 if not
    frequency: how many times a unit appears in all the units: count 2 if it appears in a phrase(sentence) for twice; count 1 if it appears in a phrase(sentence) for once, 0 if does not appear
    number_unique_term: the number of total units
    """
    
    if N==1:
        print('Unigram text framework')
        # remove duplicate words
        unigram=list(set(split_selected_word))
        unigram_frequency=[]
        unigram_presence=np.zeros(len(unigram))
        # count the frequency
        for o in range(len(unigram)):
            unigram_frequency.append(split_selected_word.count(unigram[o]))
            # count the times of presence
            for l in range(len(split_selected_text)):
                if unigram[o] in split_selected_text[l]:
                    unigram_presence[o]+=1
        gram=unigram
        presence=unigram_presence
        frequency=unigram_frequency
    else:
        print(N,"-gram text frame work")
        ngram=[]
        # classify the data by N words in one unit
        for k in range(len(split_selected_text)):
            for m in range(0,len(split_selected_text[k])-(N-1)):
                string=split_selected_text[k][m]
                for g in range(1,N):
                    string=string+" "+split_selected_text[k][m+g]
                ngram.append(str(string))
        gram=list(set(ngram))
        ngram_frequency=[]
        ngram_presence='not applicable'
        # count the frequency
        for o in range(len(gram)):
            ngram_frequency.append(ngram.count(gram[o]))
        gram=ngram
        presence=ngram_presence
        frequency=ngram_frequency
    number_unique_term=len(gram)
    return gram,presence,frequency,number_unique_term
