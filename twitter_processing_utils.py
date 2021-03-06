import re

from nltk.tokenize import WordPunctTokenizer
from bs4 import BeautifulSoup

tok = WordPunctTokenizer()
pat1 = r'@[A-Za-z0-9]+'
pat2 = r'https?://[A-Za-z0-9./]+'
combined_pat = r'|'.join((pat1, pat2))

def tweet_cleaner(text):
    ''' written by Ricky Kim(https://towardsdatascience.com/another-twitter-sentiment-analysis-bb5b01ebad90)
    '''
    soup = BeautifulSoup(text, 'lxml')
    souped = soup.get_text()
    stripped = re.sub(combined_pat, '', souped)
    try:
        clean = stripped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        clean = stripped
    letters_only = re.sub("[^a-zA-Z]", " ", clean)
    lower_case = letters_only.lower()
    words = tok.tokenize(lower_case)
    return (" ".join(words)).strip()

def apply_tweet_cleaner(text):
    if text and isinstance(text, str):
        return tweet_cleaner(text)

def add_clean_tweets_column(df, rawTweetsCol):
    df["clean_tweets"] = df[rawTweetsCol].apply(apply_tweet_cleaner)
    return df

