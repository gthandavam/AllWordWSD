'''
Created on Mar 13, 2013

@author: ganesathandavamponnuraj
'''

from nltk.corpus import wordnet as wn
from collections import defaultdict

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
    
def get_sentence_graph():
    return 

def page_rank(sentence):
    return

if __name__ == '__main__':
    print "page rank module"
    
    print wn.synsets("dog", "n") #why eclipse marking it as error ?
    
    print [sense.offset for sense in wn.synsets("dog")]
    
#    wn_pos_dist()
    
