#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Apr 11, 2017

.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Acknowledgements: 
* FastText

Evaluate embeddings generated with FastText for syntactic string similarity
'''

import unittest

import numpy as np

import settings
from load_embeddings import EmbeddingsGenerator


def evaluate_fastText_vectors(data_path, lowercase=True):
    '''
    syntactic similarity task
    '''
    
    # load fastText vector embeddings
    embs_path = settings.FAST_TEXT_VECTORS_PATH
    eg = EmbeddingsGenerator(embs_path, lowercase)
    
    # read dataset
    scores = []
    with open(data_path, 'r') as infile:
        for line in infile:
            str1, str2 = line.strip().split('\t')
            score = eg.similar_strings(str1, str2)
            print line.strip()
            print score
            scores.append(score)
    print 'Average:', np.mean(scores)



class TestFastTextVectors(unittest.TestCase):
    embs_path = settings.FAST_TEXT_VECTORS_PATH
    eg = EmbeddingsGenerator(embs_path, lowercase=True)

    # def test_read_vectors_from_file(self):
    #     assert len(self.eg.embeddings_index) == 47
    
    def test_similar_strings(self):
        # test embeddings generated via FastText for string similarity
        # similar strings: last symbol is ommitted
        # .Sentences: ['I', 'am', 'a', 'test', 'string'] ['I', 'am', 'a', 'test', 'strin']
        print (settings.TEST_STRING, settings.TEST_STRING[:-1])
        print "%.2f" % self.eg.similar_strings(settings.TEST_STRING, settings.TEST_STRING[:-1])
        assert "%.2f" % self.eg.similar_strings(settings.TEST_STRING, settings.TEST_STRING[:-1]) == '0.99'
        # different strings: all words are distinct, but 2 are similar
        # (pronouns, verb forms of to be) I am ~ It is
        # Sentences: ['I', 'am', 'a', 'test', 'string'] ['It', 'is', 'random']
        print (settings.TEST_STRING, settings.ANOTHER_TEST_STRING)
        print "%.2f" % self.eg.similar_strings(settings.TEST_STRING, settings.ANOTHER_TEST_STRING)
        assert "%.2f" % self.eg.similar_strings(settings.TEST_STRING, settings.ANOTHER_TEST_STRING) == '0.80'
        # completely different strings
        # Sentences: ['I', 'am', 'a', 'test', 'string'] ['camera', 'looks', 'great']
        print (settings.TEST_STRING, settings.VERY_DIFFERENT_TEST_STRING)
        print "%.2f" % self.eg.similar_strings(settings.TEST_STRING, settings.VERY_DIFFERENT_TEST_STRING)
        assert "%.2f" % self.eg.similar_strings(settings.TEST_STRING, settings.VERY_DIFFERENT_TEST_STRING) == '0.75'
        # same string with ommitted word delimiters
        # Sentences: ['I', 'am', 'a', 'test', 'string'] ['Iamateststring']
        print (settings.TEST_STRING, settings.TEST_STRING.replace(" ", ""))
        print "%.2f" % self.eg.similar_strings(settings.TEST_STRING, settings.TEST_STRING.replace(" ", ""))
        assert "%.2f" % self.eg.similar_strings(settings.TEST_STRING, settings.TEST_STRING.replace(" ", "")) == '0.86'


if __name__ == '__main__':
    # unittest.main()
    # evaluate_fastText_vectors(settings.SYNTACTIC_PAIRS_PATH)
    # evaluate_fastText_vectors(settings.POS_VALIDATION_DATA_PATH)
    # evaluate_fastText_vectors(settings.NEG_VALIDATION_DATA_PATH)
    evaluate_fastText_vectors(settings.ALL_VALIDATION_DATA_PATH)