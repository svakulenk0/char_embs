#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Apr 09, 2017

.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Acknowledgements: 
* SIF
* https://blog.keras.io/using-pre-trained-word-embeddings-in-a-keras-model.html
* http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/

Embed sentence into a vector space
'''
import unittest

import numpy as np
import re

from sklearn.metrics.pairwise import cosine_similarity

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


def load_embeddings():
    embeddings_index = {}
    f = open(os.path.join(GLOVE_DIR, 'glove.6B.100d.txt'))
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs
    f.close()
    print('Found %s word vectors.' % len(embeddings_index))


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
        try:
            # lowercasing
            word_id = self.dictionary[word.lower()]
            return self.embeddings[word_id]
        except:
            return []

    def embed_sentence(self, sentence):
        # tokenize: split into words on whitespace and remove punctuation
        tokens = re.findall(r"[\w']+|[.,!?;]", sentence)
        print 'Sentence:', tokens
        # print len(tokens)
        word_embs = [self.embed_word(word) for word in tokens if self.embed_word(word) != []]
        # print word_embs
        print len(tokens) - len(word_embs), 'OOV words'
        # average all word embeddings to produce sentence embedding
        return np.average(word_embs, axis=0)

    def compute_similarity(self, emb1, emb2):
        # computes cosine similarity between a pair of embeddings
        return cosine_similarity(emb1, emb2)[0][0]

    def similar_strings(self, string1, string2):
        # embeds 2 strings and computes similarity between their embeddings
        emb1 = self.embed_sentence(string1)
        emb2 = self.embed_sentence(string2)
        return self.compute_similarity(emb1, emb2)


class TestEmbeddingsGenerator(unittest.TestCase):
    ''' tests all methods of the EmbeddingsGenerator class'''
    model_path = settings.GLOVE_SMALL_PATH
    eg = EmbeddingsGenerator()
    eg.load_pretrained_vectors(model_path)

    @unittest.skip("TODO print the head only")
    def test_load_pretrained_vectors(self):
        eg = EmbeddingsGenerator()
        print eg.load_pretrained_vectors(self.model_path)

    @unittest.skip("TODO assert embedding exists")
    def test_embed_word(self):
        print self.eg.embed_word('hello')

    @unittest.skip("TODO assert embedding exists")
    def test_embed_sentence(self):
        print self.eg.embed_sentence(settings.TEST_STRING)

    def test_similar_strings(self):
        # similar strings: 1 word is different
        assert self.eg.similar_strings(settings.TEST_STRING, settings.TEST_STRING[:-1]) > 0.98
        # different strings: all words are distinct, but 2 are similar
        # (pronouns, verb forms of to be) I am ~ It is
        assert self.eg.similar_strings(settings.TEST_STRING, settings.ANOTHER_TEST_STRING) > 0.83
        # completely different strings
        assert self.eg.similar_strings(settings.TEST_STRING, settings.VERY_DIFFERENT_TEST_STRING) > 0.79


if __name__ == '__main__':
    unittest.main()
