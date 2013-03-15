'''
Created on Mar 13, 2013

@author: ganesathandavamponnuraj
'''

from nltk.corpus import wordnet as wn
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
import xml.etree.ElementTree as etree
import numbers
import gt.wsd.hw1.graphwsd.pagerank.pagerank as pr
'''
idea: 

context is sentence:
get different senses for the words in the context from wordnet 
[extension: filter the set of feasible senses parsed on POS Tag - pre-processing]
 and find co-occurrence similarity between labels of different words -> this gives us
 the edge weights

build a graph for each of the sentences that we are trying to disambiguate

choose a graph structure

and then perform pagerank on the graph (one run per instance) to yield 
the most probable sense for the word

'''

def wn_pos_dist():
    """Count the Synsets in each WordNet POS category."""
    # One-dimensional count dict with 0 as the default value:
    cats = defaultdict(int)
    # The counting loop:
    for synset in wn.all_synsets():
        cats[synset.pos] += 1
    # Print the results to the screen:
    for tag, count in cats.items():
        print tag, count
    # Total number (sum of the above):
    print 'Total', sum(cats.values())
    
def process_per_sentence(filename):
#    tree = etree.parse(filename)
#    
#    sentences = tree.findall(".//s")
#    
#    for sentence in sentences:
#        text = etree.tostring(sentence)
#        
#        print text
#    
    
    words = ['church', 'bell', 'rung', 'sunday']
    word_synsets = {}
    synset_index = {}
    index = 0
    for word in words:
        word_synsets[word] = wn.synsets(word)
        for synset in word_synsets[word]:
            synset_index[synset] = index
            print synset, index
            index += 1
#        length += len(word_synsets[word])
    graph_matrix = [[0 for i in range(index)] for j in range(index)]
    for i in range(index):
        print [graph_matrix[i][j] for j in range(index)]   

    print index

    for word1 in words:
        for word2 in words:
            if word1 != word2:
                for synset1 in word_synsets[word1]:
                    for synset2 in word_synsets[word2]:
                        sim = synset1.wup_similarity(synset2)
                        if isinstance(sim, numbers.Number) == False:
                            sim = 0
                        graph_matrix[synset_index[synset1]][synset_index[synset2]] = sim
                        graph_matrix[synset_index[synset2]][synset_index[synset1]] = sim
    
    for i in range(26):
        print [graph_matrix[i][j] for j in range(26)]   
    
    ranked_sense = pr.get_pagerank(graph_matrix)
    for word in words:
        synsets = word_synsets[word]
        max_r = 0
        max_index = -1
        for synset in synsets:
            if ranked_sense[synset_index[synset]] >= max_r:
                max_r = ranked_sense[synset_index[synset]]
                max_index = synset_index[synset]
        print max_index, max_r    
         
if __name__ == '__main__':
#    print "page rank module"
    
#    print wn.synsets("dog", "n") #why eclipse marking it as error ?
    
#    print [sense.offset for sense in wn.synsets("dog")]
    process_per_sentence("/home/aravindous/GT-CompLing/test/English/EnglishAW.test-sample.xml")
#    wn_pos_dist()
    
