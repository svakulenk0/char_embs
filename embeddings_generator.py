#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Apr 09, 2017

.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Acknowledgement: SIF

Embed sentence into a vector space
'''
import unittest

import numpy as np

import settings


def getWordmap(textfile):
    words={}
    We = []
    f = open(textfile,'r')
    lines = f.readlines()
    for (n,i) in enumerate(lines):
        i=i.split()
        j = 1
        v = []
        while j < len(i):
            v.append(float(i[j]))
            j += 1
        words[i[0]]=n
        We.append(v)
    return (words, np.array(We))


class EmbeddingsGenerator():
    '''
    Class to load pre-trained vectors and produce word/sentence embeddings
    '''
    # def __init__(self, model_path):

    def load_pretrained_vectors(self, model_path):
        '''loads GloVe model with word-level vectors'''
        (words, We) = getWordmap(model_path)
        self.dictionary = words
        self.embeddings = We

    def embed_word(self, word):
        '''
        embeds sentence using GloVe
        '''
        word_id = self.dictionary[word]
        return self.embeddings[word_id]

    def embed_sentence(self, sentence):
        # tokenize
        word_embs = [embed_word(word) for word in tokens]


class TestEmbeddingsGenerator(unittest.TestCase):
    model_path = settings.GLOVE_SMALL_PATH

    @unittest.skip("TODO print the head only")
    def test_load_pretrained_vectors(self):
        eg = EmbeddingsGenerator()
        print eg.load_pretrained_vectors(self.model_path)

    def test_embed_word(self):
        eg = EmbeddingsGenerator()
        eg.load_pretrained_vectors(self.model_path)
        print eg.embed_word('hello')


if __name__ == '__main__':
    unittest.main()
