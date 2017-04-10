#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Apr 09, 2017

.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Keep all shared variables here, e.g. test data and data paths
'''
TEST_STRING = 'I am a test string!'
OTHER_TEST_STRING = 'Yet another random string'
ANOTHER_TEST_STRING = 'It is random'
VERY_DIFFERENT_TEST_STRING = 'camera looks great'

DATA_PATH = './data/development_data.csv'
# Common Crawl (840B tokens, 2.2M vocab, cased, 300d vectors, 2.03 GB download): glove.840B.300d.zip
# https://nlp.stanford.edu/projects/glove/
GLOVE_PATH = './data/glove.840B.300d.txt' # word vector file, can be downloaded from GloVe website
GLOVE_SMALL_PATH = './data/glove.6B.50d.txt' # word vector file, can be downloaded from GloVe website
