# coding: utf-8
# This module lets you find the tf-idf of words in a web page
# (see http://en.wikipedia.org/wiki/Tf%E2%80%93idf).
# The idea is to find the words that most represent the content of this page
# wrt to a general use of the language (here, English).
# Copyright (C) 2015 Marianne Corvellec
# License: see LICENSE file


import operator

from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords


def html_file_to_text(filepath):
    """Return text contained in an html file."""
    with open(filepath) as f:
        html = f.read()
    soup = BeautifulSoup(html)
    return soup.get_text()


def tokenize_clean(text):
    """Return list of items from tokenized text."""
    tokens = word_tokenize(text.lower())
    fdist = FreqDist(tokens)
    words = [w.lower() for w in fdist.keys()
             if w not in stopwords.words('english') and w.isalpha()]
    return words


def tfidf(word, specific_fd, general_fd, unknown_default=1):
    """Return the tf-idf of a word."""
    tf = specific_fd[word]
    try:
        df = general_fd[word]
    except KeyError:
        df = unknown_default
    return tf/df


def rank_word_list(word_list, fdist, gen_dict):
    """Return a ranking list of words for a specific distribution."""
    ranked_words = {w: tfidf(w, fdist, gen_dict) for w in word_list}
    sorted_words = sorted(ranked_words.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_words


if __name__ == "__main__":
    import pprint
    # Load some input text.
    text = html_file_to_text('test.html')

    # Tokenize this text.
    our_words = tokenize_clean(text)

    # Populate a reference dictionary.
    dict0 = {}
    with open('en.txt') as f:
        ref_words = f.readlines()
        for line in ref_words:
            word, freq = line.split()
            dict0[word] = freq
    # Convert frequency string into integer.
    gen_dict = {w: int(f) for w, f in dict0.items()}

    # Get our specific frequency distribution.
    fdist = FreqDist(word_tokenize(text.lower()))

    sorted_ranking = rank_word_list(our_words, fdist, gen_dict)

    print('The 20 most frequent words are') 
    pprint.pprint(sorted_ranking[:20])
    print('The 20 least frequent words are') 
    pprint.pprint(sorted_ranking[-20:])
    print("Frequency for word 'python'")
    print(tfidf('python', fdist, gen_dict))
