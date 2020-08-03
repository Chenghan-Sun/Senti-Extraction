""" Class for Tweets Preprocessing
"""

import re
from nltk.tokenize import word_tokenize


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
    

    def _word_process(self, word):
        """ pre-processing each word into unified type
        """
        # Remove all kinds of punctuation
        clear_word = word.strip('\'"?!,.():;')

        # Convert more than 2 letter repetitions to 2 letter
        clear_word = re.sub(r'(.)\1+', r'\1\1', clear_word)

        # Remove - & '
        clear_word = re.sub(r'(-|\')', '', clear_word)
        
        # Remove http
        clear_word = re.sub('http', '',clear_word)
        # check validation of the processed word 
        word_flag = re.search(r'^[a-zA-Z][a-z0-9A-Z\._]*$', clear_word)
        if word_flag:
            return clear_word
        else:
            return None
        
        