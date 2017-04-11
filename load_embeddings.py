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

Embed sentence into a vector space using pre-trained GloVe model
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


class EmbeddingsGenerator():
    '''
    Class to load pre-trained word vectors and produce sentence-level embeddings
    '''
    def __init__(self, model_path, lowercase=False):
        self.lowercase = lowercase
        # load_embeddings from model_path file
        self.embeddings_index = {}
        with open(model_path) as f:
            for line in f:
                values = line.split()
                word = values[0]
                coefs = np.asarray(values[1:], dtype='float32')
                self.embeddings_index[word] = coefs
        print('Found %s word vectors.' % len(self.embeddings_index))

    # def load_pretrained_vectors(self, model_path):
    #     '''loads GloVe model with word-level vectors'''
    #     (words, We) = getWordmap(model_path)
    #     self.dictionary = words
    #     self.embeddings = We

    def embed_word(self, word):
        '''
        embeds sentence using GloVe
        '''
        try:
            # lowercasing
            # word_id = self.dictionary[word.lower()]
            # return self.embeddings[word_id]
            if self.lowercase:
                word = word.lower()
            return self.embeddings_index[word]
        except:
            return []

    def embed_words(self, sentence):
        # tokenize: split into words on whitespace and remove punctuation
        # tokens = re.findall(r"[\w']+|[.,!?;]", sentence)
        # tokenize: split on whitespace only
        tokens = sentence.split(' ')
        # print 'Sentence:', tokens
        # print len(tokens)
        # do not consider OOV words!
        word_embs = [self.embed_word(word) for word in tokens if self.embed_word(word) != []]
        # print word_embs
        oov_words = len(tokens) - len(word_embs)
        if oov_words > 0:
            print len(tokens) - len(word_embs), 'OOV words'
        return word_embs

    def embed_words_avrg(self, sentence):
        word_embs = self.embed_words(sentence)
        # average all word embeddings to produce sentence embedding
        return np.average(word_embs, axis=0)

    def compute_similarity(self, emb1, emb2):
        # computes cosine similarity between a pair of embeddings
        return cosine_similarity(emb1, emb2)[0][0]

    def similar_strings(self, string1, string2):
        # embeds 2 strings and computes similarity between their embeddings
        emb1 = self.embed_words_avrg(string1).reshape(1, -1)
        emb2 = self.embed_words_avrg(string2).reshape(1, -1)
        return self.compute_similarity(emb1, emb2)

    def embed_words_matrix(self, sentence, embedding_dim=settings.EMBEDDING_DIM):
        # prepare embedding matrix
        # no restriction on the maximum number of words to embed
        # num_words = min(MAX_NB_WORDS, len(word_index))
        word_embs = self.embed_words(sentence)
        embedding_matrix = np.zeros((len(word_embs), embedding_dim))
        for i, word_embedding in enumerate(word_embs):
            # if embedding_vector is not None:
                # words not found in embedding index will be all-zeros.
            # do not consider OOV words
            embedding_matrix[i] = word_embedding
        return embedding_matrix


# class TestGloVeVectors(unittest.TestCase):
#     embs_path = settings.GLOVE_SMALL_PATH
#     eg = EmbeddingsGenerator(embs_path)

#     @unittest.skip("TODO assert embedding exists")
#     def test_embed_word(self):
#         print self.eg.embed_word('hello')

#     @unittest.skip("TODO assert embedding exists")
#     def test_embed_sentence_avrg(self):
#         print self.eg.embed_words_avrg(settings.TEST_STRING)

#     @unittest.skip("TODO assert embeddings matrix size")
#     def test_embed_words_matrix(self):
#         print self.eg.embed_words_matrix(settings.TEST_STRING)

#     # @unittest.skip("temporal")
#     def test_similar_strings(self):
#         # test embeddings from GloVe for string similarity: OOV words get NaN representation
#         # similar strings: 1 word is different
#         assert self.eg.similar_strings(settings.TEST_STRING, settings.TEST_STRING[:-1]) < 0.99
#         # different strings: all words are distinct, but 2 are similar
#         # (pronouns, verb forms of to be) I am ~ It is
#         assert self.eg.similar_strings(settings.TEST_STRING, settings.ANOTHER_TEST_STRING) < 0.84
#         # completely different strings
#         assert self.eg.similar_strings(settings.TEST_STRING, settings.VERY_DIFFERENT_TEST_STRING) < 0.8
#         # same string with ommitted word delimiters => OOV word, 1 common word '!'
#         # assert self.eg.similar_strings(settings.TEST_STRING, settings.TEST_STRING.replace(" ", "")) < 0.75


# class TestFastTextVectors(unittest.TestCase):
#     embs_path = settings.FAST_TEXT_VECTORS_PATH
#     eg = EmbeddingsGenerator(embs_path)

#     def test_read_vectors_from_file(self):
#         assert len(self.eg.embeddings_index) == 15


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestGloVeVectors)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestFastTextVectors)
    all_tests = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(all_tests)
