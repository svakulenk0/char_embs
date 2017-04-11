# Comprendes

(Comprend~o/es/e/emos/an) #wedntreadwords

Character- and word-level embeddings for short texts.

Goal: decoupling and recombining syntactic (character-level) and semantic (contextual) similarity in distributed string embeddings.

The idea is to:

	* capture the signal for syntactic similarity on the character level.

	* capture the signal for semantic (contextual) similarity, e.g. via word-embeddings, to gain access to the semantic space structure beyond syntactic similarity.

	* decypher (model) the meaning for (embed) OOV strings


## Motivation/Applications

* Social media (misspellings)

* Identifiers e.g. column headers in tables or databases, Twitter handles, etc.

* Multilingual data (linguistic similarities across languages e.g. italian/spanish)


## Requirements

The model has to tolerate the following corruptions in textual data by indicating syntactic similarity 

* upper/lower casing
* spacing (presence or absence as well as the variety of the word-level delimiters)
* omition/inflaction of substrings
* reordering of substrings


## Baseline

* FastText

## Results

* FastText requires tokens to be lower-cased

Development data:


TODO explore the threshold! generate negative samples!

('I am a test string', 'camera looks great')
similarity threshold on the unrelated strings: 0.75

('I am a test string', 'I am a test strin')
0.99
('I am a test string', 'It is random')
0.80
('I am a test string', 'Iamateststring')
0.86


#wedontreadwords	we do not read words
0.780289
NUTS2	NUTS code
0.769711
LAU2_CODE	code
0.856604
LAU2_CODE	NUTS code
0.757809
LAU2_NAME	name
0.850325
INTERNAL_MIG_IMMIGRATION	internal immigration
0.971787
INTERNAL_MIG_IMMIGRATION	international immigration
0.940776
INTERNATIONAL_MIG_IMMIGRATION	international immigration
0.990686
INTERNATIONAL_MIG_IMMIGRATION	internal immigration
0.878337
IMMIGRATION_TOTAL	total immigration
0.909382
IMMIGRATION_TOTAL	total emigration
0.875539
INTERNAL_MIG_EMIGRATION	internal emigration
0.974324
INTERNAL_MIG_EMIGRATION	internal immigration
0.955661
INTERNATIONAL_MIG_EMIGRATION	international emigration
0.989659
INTERNATIONAL_MIG_EMIGRATION	international immigration
0.973965
EMIGRATION_TOTAL	total emigration
0.918322
EMIGRATION_TOTAL	total immigration
0.900769

Fail:
#CMABRIGDEUINERVTISYEFECT	Cambridge university effect
0.715672

Average: 0.9 on positive examples excluding cambridge and year
Average: 0.897551 on negative examples


## Acknowledgements

* [SIF][]

* [Francois Chollet. Using pre-trained word embeddings in a Keras model][https://blog.keras.io/using-pre-trained-word-embeddings-in-a-keras-model.html]

* [Christian S. Perone. Machine Learning :: Cosine Similarity for Vector Space Models][http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/]

## Related Work

### Character-based Neural Networks

* Robsut wrod reocginiton via semi-character recurrent neural network. 2017 [PDF][https://arxiv.org/pdf/1608.02214.pdf]

### OOV words representation

* Paraphrasing Out-of-Vocabulary Words with Word Embeddings and Semantic Lexicons for Low Resource Statistical Machine Translation. LREC. 2016 [PDF][http://www.lrec-conf.org/proceedings/lrec2016/pdf/359_Paper.pdf]

* Mapping Unseen Words to Task-Trained Embedding Spaces. ACL. 2016 [PDF][https://aclweb.org/anthology/W/W16/W16-1612.pdf]

* Resolving Out-of-Vocabulary Words with Bilingual Embeddings in Machine Translation. 2016

* A Joint Model for Word Embedding and Word Morphology. [PDF][https://arxiv.org/pdf/1606.02601.pdf]

### Morphology and subword representation

* Morphological Smoothing and Extrapolation of Word Embeddings [PDF][https://pdfs.semanticscholar.org/7bab/314194e872eba7157cf0803df4f6e6b67d1f.pdf]

* Enriching Word Vectors with Subword Information [PDF][https://arxiv.org/pdf/1607.04606.pdf]

* A joint many-task model: Growing a neural network for multiple NLP tasks. 2016 [PDF][https://arxiv.org/pdf/1611.01587.pdf][Code][https://github.com/rajarsheem/joint-many-task-model]

### Language Modeling

* Character-Aware Neural Language Models (AAAI 2016) [Code][https://github.com/yoonkim/lstm-char-cnn]

* Generating text with recurrent neural networks. 2011

* Multiplicative LSTM for sequence modelling

### Text Similarity

* CHARAGRAM: Embedding Words and Sentences via Character n-grams ACL 2016 [PDF][https://aclweb.org/anthology/D16-1157]

* A Simple but Tough-to-Beat Baseline for Sentence Embeddings. ICLR 2017

* Short Text Similarity with Word Embeddings. [PDF][https://staff.fnwi.uva.nl/m.derijke/wp-content/papercite-data/pdf/kenter-short-2015.pdf]

### Text Classification

* Character-level Convolutional Networks for Text Classification	nips		2015
[PDF][https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf]

* Bag of Tricks for Efficient Text Classification

### Text Clustering

* Semi-supervised Clustering for Short Text via Deep Representation Learning

* Self-Taught Convolutional Neural Networks for Short Text Clustering

* Short Text Clustering via Convolutional Neural Networks

### Information Extraction

* Deep learning for character-based information extraction. 2014

### Evaluation

* Problems With Evaluation of Word Embeddings Using Word Similarity Tasks
