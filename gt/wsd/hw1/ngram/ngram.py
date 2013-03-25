'''


Created on Mar 20, 2013

@author: Omar Khazamov
'''
import nltk
import re
from sets import Set
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
import xml.etree.ElementTree as etree
from gt.wsd.hw1.graphwsd.lesk_test import *

filename='/home/user/Downloads/task17-test+keys/test/English/small_EnglishAW.test.xml'

def get_sentence(tree,key):  
   sentence=""
   text_id=""
   for text in tree.findall("//s"):
     #print text_id=
     for head in text.iter():
     #print head
      if head.tag=="head": 
       if head.attrib['id']==key:
              for s in text.itertext():
                  sentence+=s
   sentence=sentence.replace("\n", " ")
   return sentence  


def get_sentence_map(tree):
    text_id=""
    dict = {}
   
    for head in tree.findall("//head"):
             #   if head.attrib['id']!=None:
                    l=split_syn_dots(head.attrib['id'])
                    if (dict.get(l[0]+l[1])!=None):
                            #if (head.attrib['id'])
                            dict[l[0]+l[1]]+=","+head.attrib['id']
                    else:
                            dict[l[0]+l[1]]=head.attrib['id']
                  #sentence+=s
                  
   #sentence=sentence.replace("\n", " ")
    return dict

def get_sentence_map_full(tree):
    text_id=""
    dict = {}
    full_dict = {}
    for s in tree.findall("//s"):
           for head in s.findall("//head"):
            
             #   if head.attrib['id']!=None:
                    l=split_syn_dots(head.attrib['id'])
                    if (full_dict.get(l[0]+l[1])!=None):
                        full_dict[l[0]+l[1]]=s.itertext()
                    if (dict.get(l[0]+l[1])!=None):
                            #if (head.attrib['id'])
                            dict[l[0]+l[1]]+=","+head.attrib['id']
                            
                    else:
                            dict[l[0]+l[1]]=head.attrib['id']
                            
                  #sentence+=s
                  
   #sentence=sentence.replace("\n", " ")
    return dict,full_dict

def get_wsd_input_data(tree):
    
        
# xml file comes without a namespace; so looking up for all the head tags within the document,
#without specifying the namespace
#Ref: http://getpython3.com/diveintopython3/xml.html#xml-parse
    
    heads = tree.findall("//head")    
    
    ret_dictionary = {}
    
    for head in heads:
#        print head.attrib['id']," " + head.text
        ret_dictionary[head.attrib['id']] = head.text
    return ret_dictionary    
        
#breaking up on n_grams
def ngram(words):
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = nltk.collocations.BigramCollocationFinder.from_words(words)
    finder.apply_freq_filter(3)
    finder.apply_word_filter(filter_stops)
    matches1 = finder.nbest(bigram_measures.pmi, 5)
    return matches

 
print "NGRAM MODEL WSD"
tree = etree.parse(filename)
sentence_map=get_sentence_map(tree)
dicti={}
dicti=get_wsd_input_data(tree)
for key in sentence_map.iterkeys():
  #promise won't do anything like that anymore, just let me  get things working
    full_sentence=get_sentences(tree,key)
    for word_k in sentence_map[key].split(","):
        sentence+=dicti[word_k]
    print ngram(full_sentence)
  
  #sentence.join('')

  #word=wn.morphy(dicti[key].lower())
  #print word,dictionary[key]
  #sentence=get_sentence(tree,key)
    

    
