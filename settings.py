#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Apr 09, 2017

.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Keep all shared variables here, e.g. test data and data paths
'''
# test strings
TEST_STRING = 'I am a test string'
# TEST_STRING = 'I am a test string!'
OTHER_TEST_STRING = 'Yet another random string'
ANOTHER_TEST_STRING = 'It is random'
VERY_DIFFERENT_TEST_STRING = 'camera looks great'

# embeddings
# Common Crawl (840B tokens, 2.2M vocab, cased, 300d vectors, 2.03 GB download): glove.840B.300d.zip
# https://nlp.stanford.edu/projects/glove/
GLOVE_PATH = './embeddings/glove.840B.300d.txt' # word vector file, can be downloaded from GloVe website
GLOVE_SMALL_PATH = './embeddings/glove.6B.50d.txt' # word vector file, can be downloaded from GloVe website
# file_path = os.path.join(GLOVE_DIR, 'glove.6B.100d.txt')
FAST_TEXT_VECTORS_PATH = './embeddings/fastText_vectors.txt'

# EMBEDDING_DIM = 100
EMBEDDING_DIM = 50  # for GLOVE_SMALL_PATH: glove.6B.50d embeddings

# data: string pairs
IN_FILE_PATH = './data/seed_strings.txt'
POS_SYNTACTIC_PAIRS_PATH = './data/similar_string_pairs.txt'
# NEG_SYNTACTIC_PAIRS_PATH = './data/dissimilar_string_pairs.txt'
POS_VALIDATION_DATA_PATH = './data/pos_development_data.txt'
NEG_VALIDATION_DATA_PATH = './data/neg_development_data.txt'
ALL_VALIDATION_DATA_PATH = './data/development_data.txt'
