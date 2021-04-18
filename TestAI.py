import json
import pandas as pd
import nltk
import re
import string
# nltk.download([
#     "names",
#     "stopwords",
#     "state_union",
#     "twitter_samples",
#     "movie_reviews",
#     "averaged_perceptron_tagger",
#     "vader_lexicon",
#     "punkt",
# ])
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer


# words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
stopwords = nltk.corpus.stopwords.words("english")
# words = [w for w in words if w.lower() not in stopwords]


# text = """For some quick analysis, creating a corpus could be overkill. If all you need is a word list, there are simpler ways to achieve that goal."""


# words: list[str] = nltk.word_tokenize(tweets)
# words: list[str] = nltk.word_tokenize(str)
# fd = nltk.FreqDist(words)

# text = nltk.Text(nltk.corpus.state_union.words())
# text.concordance("america", lines=5)

# concordance_list = text.concordance_list("america", lines=2)

# print(words)


def clean(word):
    print(word)
    re.sub("#[0-9A-Za-Z]+", "", word)  # delete hastags
    re.sub("@[0-9A-Za-Z]+", "", word)  # remove @'s
    re.sub("\\n", "", word)  # remove any new lines
    re.sub("https?:\/\/S+", "", word)  # remove hyperlinks
    return word
