# caption-words
Utility to find specific or over-represented words in (technical) documents (pages, documentation...)

This module lets you find the tf-idf of words in a web page
(see [Wikipedia](http://en.wikipedia.org/wiki/Tf%E2%80%93idf)).
The idea is to find the words that most represent the content of this page
wrt to a general use of the language (here, English).

## Dependencies
`pip install` the following:
```
beautifulsoup4==4.3.2
nltk==3.0.2
```
Then download `nltk` data:
```
$ sudo python -m nltk.downloader -d /usr/share/nltk_data all
```

## Running
You can run `term_frequency.py` as a standalone script:
```
python3 term_frequency.py
```

## Data
Input files are provided for convenience.
### Frequency Word Lists
[https://invokeit.wordpress.com/frequency-word-lists/](https://invokeit.wordpress.com/frequency-word-lists/)
### Test file
Page [https://docs.python.org/3/](https://docs.python.org/3/)
