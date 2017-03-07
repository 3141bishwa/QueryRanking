"""
Classifying queries based on NAPCS Classification System
Author: Bishwa Silwal
Date: March 6, 2017
"""

import pandas as pd
import nltk
import gensim
import operator


# Download necessary packages to use NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


#Finds Nouns in a phrase/sentence excluding certain words
def getNouns(sentence, exclude_words):
    nouns = []
    for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS') and word not in exclude_words:
            nouns.append(word)
    return nouns

#Find a similarity ranking based on the words
def get_similarity(query, list_of_words):
    total_score = 0
    for word in list_of_words:
        try:
            score = model.similarity(word, query)
            total_score += score
        except KeyError:
            #Ignores the words that it can't find in the model
            print "Not Found", word
    return total_score

# Returns the top 5 categories with highest scores
def highest_five_values(dictionary):
    return sorted(dictionary.iteritems(), key=operator.itemgetter(1), reverse=True)[:5]


if __name__ == "__main__":
    # Excluding these words for the similarities since they are too generic
    # and appear quite frequently in all sections
    exclude_nouns = ["services", "products"]

    sections_csv = pd.read_csv("sections.csv")
    data = [tuple(x) for x in sections_csv[["2017 NAPCS Code" ,"Title"]].values]

    score_dict = {}

    model = gensim.models.KeyedVectors.load_word2vec_format("data.bin.gz", binary = True)

    want_another_word = True
    while want_another_word:
        query = raw_input("Choose a word: ")

        for section_id, section in data:
            nouns = getNouns(section, exclude_nouns)
            score = get_similarity(query, nouns)
            score_dict[section] = score

        for section_name, score in highest_five_values(score_dict):
            print section_name, score

        want = raw_input("Want to query another word? Answer T for True and F for False: ")

        if want == "T":
            want_another_word = True
        else:
            want_another_word = False
