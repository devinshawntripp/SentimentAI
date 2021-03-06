import json
import pandas as pd
import nltk
import re
import string
import os
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
from transformers import pipeline

sentiment_classifier = pipeline('sentiment-analysis')


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

testFile = os.getenv('TEST_FILE')

# Opening JSON file
tweets = []
for line in open(testFile, 'r'):
    tweets.append(json.loads(line))


# returns JSON object as
df = pd.DataFrame(tweets, columns=['overall', 'reviewText'])


# print(df.head(5))


# altText = [w for w in tweets]

# print(altText)
stemmer = PorterStemmer()
# example of lemmatization
lemmatizer = WordNetLemmatizer()

# print(df['summary'])
# df = df.drop(['reviewTime', 'reviewerID', 'asin',
#              'unixReviewTime', 'style'], axis=1)
# wordsList = [str(df['reviewText'])]

# print(df.head(10))


def clean(word):
    strWord = str(word)
    re.sub("#[A-Za-z0-9]+", "", strWord)  # delete hastags
    re.sub("@[A-Za-z0-9]+", "", strWord)  # remove @'s
    re.sub("\\n", "", strWord)  # remove any new lines
    re.sub("https?:\/\/S+", "", strWord)  # remove hyperlinks
    return strWord


new_df = pd.DataFrame()

df['cleanedText'] = df['reviewText'].apply(clean)
# print(df['cleanedText'])

wordList = df['cleanedText'].values.tolist()


results = sentiment_classifier(wordList)

print(results)

# wordList = new_df['reviews'].toList()

# print(new_df.head(4))


# for someWord in wordsList:
#     # print(someWord)
#     # someWord = " ".join(
#     #     [word for word in someWord.split() if word not in stopwords])
#     # encoding the text to ASCII format
#     someWord = someWord.encode(encoding="ascii", errors="ignore")
#     # decoding the text
#     someWord = someWord.decode()
#     someWord = re.sub("@\S+", "", someWord)
#     someWord = re.sub("\$", "", someWord)
#     someWord = re.sub("https?:\/\/.*[\r\n]*", "", someWord)
#     someWord = re.sub("#", "", someWord)
#     someWord = someWord.replace("\\n", "")
#     someWord = someWord.replace("\\", "")
#     someWord = someWord.replace("...", "")
#     someWord = re.sub(r"[0-9]+", '', someWord)
#     punct = set(string.punctuation)
#     someWord = "".join([ch for ch in someWord if ch not in punct])
#     lemmatizer.lemmatize(someWord)
#     totalWords.append(someWord)
#     # print(someWord)

# totalWords = [i for item in totalWords for i in item.split()]


# print(totalWords)
