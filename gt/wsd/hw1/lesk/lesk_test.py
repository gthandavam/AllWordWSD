'''
Created on Mar 13, 2013

@author: ganesathandavamponnuraj
'''
#!/usr/bin/python
import nltk
from sets import Set
from nltk.corpus import wordnet as wn

def get_context_words(sentence):          #extracts content words and converts them to the base form
    tokens=nltk.word_tokenize(sentence)
    text = nltk.Text(tokens)
    words = [wn.morphy(w.lower()) if wn.morphy(w.lower())!=None else w.lower() for w in text]
    return words


def computeoverlap(sig1,sig2):            #need to know how many words have in common
    overlap=set.intersection(sig1,sig2)
    return len(overlap)  
 
sentence="The bass line of the song is too weak"
word="bass"
context_original=set([])
# My first python program
for w in get_context_words(sentence):
    context_original.add(w)

print "Lesk \n"
best_sense=wn.lemmas(word)[0].synset.definition #best sense    #most frequent sense is a default one

max_overlap=0



for lemma in wn.lemmas(word):
    context_int=set([])
    for example in lemma.synset.examples:         #crawl through all definitions and examples
        print "Lemma: "+lemma.name+"\n"
        print "Example: "+ example+"\n"
        for w in get_context_words(example):
            context_int.add(w)
    for w in get_context_words(lemma.synset.definition):
        print context_int
        context_int.add(w)
        overlap=computeoverlap(context_original,context_int)
        
    if overlap>max_overlap:
        max_overlap=overlap
        best_sense=lemma.synset.definition

print "\n The best sense is: \n "+best_sense