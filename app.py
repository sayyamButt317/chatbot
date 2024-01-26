import nltk
#nltk.download('punkt')
from nltk.steam.porter import PorterStemmer
stemmer = PorterStemmer()
def tokenize(sentance):
    return nltk.word_tokenize(sentance)
    
def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,all_words):
    pass
