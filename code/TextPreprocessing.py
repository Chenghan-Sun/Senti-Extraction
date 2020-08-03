""" Class for Tweets Preprocessing
"""

import re
from nltk.tokenize import word_tokenize
import pandas as pd


class TweetPreprocess(object):
    """ Tweets Preprocessing class including additional methods for analysis
    Currently only support analysis for a piece of single tweet
    """
    
    def __init__(self, tweet):
        self.tweet = tweet
        
    def process_tweet(self, ):
        """ Ensemble methods for single tweet processing 
        """
        words = word_tokenize(self.tweet)
        for word in words:
            clear_word = self._word_process(word)
            print(clear_word)
        return clear_word
    
    def _detect_tweet(self, ):
        """ 
        """ 
        pass 

    def _word_process(self, word):
        """ pre-processing each word into unified type
        """
        # Remove all kinds of punctuation
        clear_word = word.strip('\'"?!,.():;')

        # Convert more than 2 letter repetitions to 2 letter
        clear_word = re.sub(r'(.)\1+', r'\1\1', clear_word)

        # Remove - & '
        clear_word = re.sub(r'(-|\')', '', clear_word)

        # check validation of the processed word 
        word_flag = re.search(r'^[a-zA-Z][a-z0-9A-Z\._]*$', clear_word)
        if word_flag:
            return clear_word
        else:
            return None

        
def process_to_csv(process_df, feature, clean_csv_path):
    """ Ensemble method for processing multiple tweets in dataframe (df)
    Params:
        process_df: the df to be processed
        feature: feature (colunm) of the df, use 'text' or 'selected_text'
        clean_csv_path: directory of written out csv file
    Return:
        saved_csv: csv file save to clean_csv_path
    """
    processed_df = process_df.copy()
    
    for i, tweet in enumerate(process_df[feature]):
        if type(tweet) == str:
            processer = TweetPreprocess(tweet)
        else:
            raise Exception('The tweet must be str!')
            
        clean_tweet = processer.process_tweet()
        processed_df[feature][i] = clean_tweet
        
    # save as a csv file 
    processed_df.to_csv(clean_csv_path)
    return processed_df
