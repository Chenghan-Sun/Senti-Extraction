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
        # Load in given tweet
        tweet = self.tweet
        # Convert to lower case
        tweet = tweet.lower()
        # Replaces URLs with the word URL
        # TODO: May delete it later
        tweet = re.sub(r'((www\.[\S]+)|(https?://[\S]+))', ' URL ', tweet)
        # Replace @handle with the word USER_MENTION
        tweet = re.sub(r'@[\S]+', 'USER_MENTION', tweet)
        # Replaces #hashtag with hashtag
        tweet = re.sub(r'#(\S+)', r' \1 ', tweet)
        # Remove RT (retweet)
        tweet = re.sub(r'\brt\b', '', tweet)
        # Replace 2+ dots with space
        tweet = re.sub(r'\.{2,}', ' ', tweet)
        # Strip space, " and ' from tweet
        tweet = tweet.strip(' "\'')
        # Replace multiple spaces with a single space
        tweet = re.sub(r'\s+', ' ', tweet)
        
        # Pass processed tweet back to object
        self.tweet = tweet
        
        clean_tweet = []
        words = word_tokenize(self.tweet)
        for word in words:
            clear_word = self._word_process(word)
            clean_tweet.append(clear_word)
            
        clean_tweet_str = ' '.join(clean_tweet)
        return clean_tweet_str
    
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

        
"""
Emsemble Method
"""

def process_to_csv(process_df, feature, clean_csv_path):
    """ Ensemble method for processing multiple tweets in dataframe (df)
    Params:
        process_df: the df to be processed
        feature: feature (colunm) of the df, use 'text' or 'selected_text'
        clean_csv_path: directory of written out csv file
    Return:
        saved_csv: csv file save to clean_csv_path
    """
    # copy the processed df from original df 
    processed_df = process_df.copy()
    
    for i, tweet in enumerate(process_df[feature]):
        if type(tweet) == str:
            processer = TweetPreprocess(tweet)
        else:
            raise Exception('The tweet must be str!')
            
        # call the processer class 
        clean_tweet = processer.process_tweet()
        processed_df[feature][i] = clean_tweet  
        
    # save as a csv file 
    processed_df.to_csv(clean_csv_path)
    return processed_df
