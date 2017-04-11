#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Apr 09, 2017

.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Generate artificial dataset for character-level embeddings
'''
import unittest

import csv

import editdistance

import settings


def generate_strings(seed_string):
    '''the first string in the output array is the original input string'''
    # generated_strings = [seed_string]
    generated_strings = []
    # * upper/lower casing
    # change case: all up, all low
    generated_strings.append(seed_string.lower())
    generated_strings.append(seed_string.upper())
    # * spacing (presence or absence as well as the variety of the word-level delimiters)
    # remove all spaces
    generated_strings.append(seed_string.replace(" ", ""))
    # replace all spaces with _
    generated_strings.append(seed_string.replace(" ", "_"))

    # * omition/inflaction of substrings
    # randomly remove characters
    # remove the last character from the input string
    generated_strings.append(seed_string[:-1])
    # randomly add characters
    # repeat the last character 
    generated_strings.append(seed_string + seed_string[-1])

    # * reordering of substrings
    # randomly reorder characters
    return generated_strings


def generate_syntactic_similarity_corpus(seeds_path, results_path):
    # read input file with seed strings
    with open(seeds_path, 'r') as infile, open(results_path, 'w') as outfile:
        for seed_string in infile:
            # generate corrupted strings
            # and write the string pairs into the output file
            generated_strings = generate_strings(seed_string.strip())
            print generated_strings
            outfile.writelines([seed_string.strip()+'\t'+new_string+'\n' for new_string in generated_strings])


def check_str_similarity(string1, string2):
    '''
    edit distance (Levenshtein distance)
    '''
    return editdistance.eval(string1, string2)
    # check similarity with the original string

    # check similarity with a different string


def embed_string(string):
    '''
    generates character-level/word-level embedding for the input string
    '''
    pass


def check_emb_similarity(emb1, emb2):
    '''
    cosine similarity
    '''
    pass
    # check similarity with the original string

    # check similarity with a different string


def blend_strings(string1, string2):
    # transform string1 into string2 and vice versa via edit distance
    # discover the similarity boundary!
    pass


def load_data(data_path):
    '''
    read similar string pairs from CSV
    '''
    with open(data_path) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for oov, full in reader:
            print '\n'.join(['\nPair:', oov, full])
            print 'Levenshtein distance:', check_str_similarity(oov, full)

# encode sentences using pre-trained embeddings

class TestDataGenerator(unittest.TestCase):
    def test_generate(self):
        for generated_str in generate_strings(settings.TEST_STRING):
            print generated_str

    def test_load_data(self):
        load_data(settings.DATA_PATH)

    def test_check_str_similarity(self):
        print check_str_similarity(settings.TEST_STRING, settings.ANOTHER_TEST_STRING)


if __name__ == '__main__':
    # unittest.main()
    generate_syntactic_similarity_corpus(settings.IN_FILE_PATH, settings.POS_SYNTACTIC_PAIRS_PATH)
