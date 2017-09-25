#!/usr/bin/env python
# coding=utf-8

import nltk

def test_nltk():
    """"""
    sentence = """
    At eight o'clock on Thursday morning
    ... arthur didn't fell very good.
    """

    tokens = nltk.word_tokenize(sentence)

    print(tokens)


if __name__ == "__main__":
    """"""
    test_nltk()
