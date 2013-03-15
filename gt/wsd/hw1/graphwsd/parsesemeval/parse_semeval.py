'''
Created on Mar 12, 2013

@author: ganesathandavamponnuraj
'''
import xml.etree.ElementTree as etree
from nltk.corpus import wordnet as wn


'''
    @param - filename @type string -> filename path that contains the sem-eval test data [EnglishAW.text.xml file]
    @return - returns a dictionary: key -> id of the head tag in the sem-eval task 17 document @type string
                                    value-> word to be disambiguated @type string
'''
def get_words_for_disambiguation_test_data(filename):
    tree = etree.parse(filename)
        
# xml file comes without a namespace; so looking up for all the head tags within the document,
#without specifying the namespace
#Ref: http://getpython3.com/diveintopython3/xml.html#xml-parse
    heads = tree.findall("//head")    
    
    ret_dictionary = {}
    
    for head in heads:
#        print head.attrib['id']," " + head.text
        ret_dictionary[head.attrib['id']] = head.text
        
    return ret_dictionary    

def find_similarity(word1, word2):
    return

def get_sentences(filename):
    #in-memory - bad 
    tree = etree.parse(filename)
    
    sentences = tree.findall("//s")
    
    for sentence in sentences:
    
        heads = sentence.findall("head")
        
        print etree.tostring(sentence)
        
        if( len(heads) ):#non zero length - consider a sentence otherwise just ignore
            print "non zero number of heads"
        
if __name__ == '__main__':
    dictionary = get_words_for_disambiguation_test_data('/home/aravindous/GT-CompLing/test/English/EnglishAW.test.xml');
    for key in dictionary.keys():
        print key," " + dictionary[key]
        
#    get_sentences("/Users/ganesathandavamponnuraj/Downloads/task17-test+keys/test/English/test_xml.xml");
    