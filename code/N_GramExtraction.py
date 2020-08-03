def nGram(split_selected_word,split_selected_text,N):
    if N==1:
        print('Unigram text framework')
        unigram=list(set(split_selected_word))
        unigram_frequency=[]
        unigram_presence=np.zeros(len(Unigram))
        for o in range(len(Unigram)):
            unigram_frequency.append(split_selected_word.count(unigram[o]))
            for l in range(len(split_selected_text)):
                if unigram[o] in split_selected_text[l]:
                    unigram_presence[o]+=1
        gram=unigram
    else:
        ngram=[]
        for k in range(len(split_selected_text)):
            for m in range(0,len(split_selected_text[k])-(N-1)):
                string=split_selected_text[k][m]
                for g in range(1,N):
                    string=string+" "+split_selected_text[k][m+g]
                ngram.append(str(string))
        gram=ngram
    return gram