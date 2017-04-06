"""Author: Bishwa Silwal
Classifying queries based on NAPCS Classification System
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

#Find a similarity ranking based on the words by computing the average similarity
# score for a word in a category
def get_avg_similarity(query, list_of_words):
    total_score = 0
    if len(list_of_words) != 0:
        for word in list_of_words:
            try:
                score = model.similarity(word, query)
                total_score += score
            except KeyError:
                #Ignores the words that it can't find in the model
                #print "Not Found", word
        return total_score/len(list_of_words)
    else:
        return 0

# Returns the maximum score
def get_max_similarity(query, list_of_words):
    max_score = 0
    for word in list_of_words:
        try:
            score = model.similarity(word, query)
            if score > max_score:
                max_score = score
        except KeyError:
            #Ignores the words that it can't find in the model
            #print "Not Found", word
    return max_score

# Returns the top 5 categories with highest scores
def highest_five_values(dictionary):
    return sorted(dictionary.iteritems(), key=operator.itemgetter(1), reverse=True)[:5]


if __name__ == "__main__":
    # Excluding these words for the similarities since they are too generic
    # and appear quite frequently in all sections
    exclude_nouns = ["services", "products"]

    structure_csv = pd.read_csv("final_structure.csv")
    structure_csv["2017 NAPCS Code"] = structure_csv["2017 NAPCS Code"].astype('str')

    #Get NAPCS Categories which are at the bottom of the Structure Hierarchy
    structure_csv = structure_csv[structure_csv["2017 NAPCS Code"].str.len() == 11]

    data = [tuple(x) for x in structure_csv[["2017 NAPCS Code" ,"Title"]].values ]

    print structure_csv

    score_dict_first_method = {}
    score_dict_second_method = {}

    model = gensim.models.KeyedVectors.load_word2vec_format("data.bin.gz", binary = True)

    want_another_word = True

    while want_another_word:
        query = raw_input("Choose a word: ")

        #Checks if word exists in the vocabulary
        if query in model.vocab:
            for section_id, section in data:

                #Extract keywords for each category ignoring keywords which repeatedly occur
                nouns = getNouns(section, exclude_nouns)


                score_first_method = get_avg_similarity(query, nouns)
                score_second_method = get_max_similarity(query, nouns)

                score_dict_first_method[section] = score_first_method
                score_dict_second_method[section] = score_second_method

            print "Ranking Method 1: Average similarity score for a category:"
            print "=========================================================="
            for section_name, score in highest_five_values(score_dict_first_method):
                print section_name, score

            print ""
            print "Ranking Method 1: Max simiarity score for a category:"
            print "=========================================================="
            for section_name, score in highest_five_values(score_dict_second_method):
                print section_name, score


            want = raw_input("Want to query another word? Answer T for True and F for False: ")

            if want == "T":
                want_another_word = True
            else:
                want_another_word = False
        else:
            print "Word not found. Try again."
