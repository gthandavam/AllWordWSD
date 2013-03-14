'''
Created on Mar 13, 2013

@author: ganesathandavamponnuraj
'''

from nltk.corpus import wordnet as wn
from collections import defaultdict

'''
idea: get different senses for the words from wordnet
[extension: filter the set of feasible senses parsed on POS Tag - pre-processing]
 and attach
a distribution for the word label pairs

build a graph for each of the sentences that we are trying to disambiguate

and then perform pagerank on the graph (one run per instance) to yield 
the most probably sense for the word

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

if __name__ == '__main__':
    print "preparing the graph for deep-learning"
    print wn.synsets("dog", "n") #why eclipse marking it as error ?
    
    print [lemma.name for lemma in wn.synset('dog.n.01').lemmas]
    
#    wn_pos_dist()
    
