# caption-words
Utility to find specific or over-represented words in (technical) documents (pages, documentation...)

This module lets you find the tf-idf of words in a web page
(see [Wikipedia](http://en.wikipedia.org/wiki/Tf%E2%80%93idf)).
The idea is to find the words that most represent the content of this page
wrt to a general use of the language (here, English).

## Setup

    $ virtualenv --python=python3.6 ~/.virtualenv/caption-words
    $ source ~/.virtualenv/caption-words/bin/activate
    $ pip install -r requirements.txt
    $ deactivate

## Data

Download `nltk` data into a system-wide directory:

    $ sudo python -m nltk.downloader -d /usr/share/nltk_data all

Input files are provided for convenience.

### Frequency Word Lists
[https://invokeit.wordpress.com/frequency-word-lists/](https://invokeit.wordpress.com/frequency-word-lists/)

    $ unzip en-2012.zip

### Test file

File `test.html` is page [https://docs.python.org/3/](https://docs.python.org/3/).

## Running

You can run `term_frequency.py` as a standalone script:

    $ source ~/.virtualenv/caption-words/bin/activate
    $ python term_frequency.py
