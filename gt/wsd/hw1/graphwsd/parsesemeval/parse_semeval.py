'''
Created on Mar 12, 2013

@author: ganesathandavamponnuraj
'''
import xml.etree.ElementTree as etree

if __name__ == '__main__':
    tree = etree.parse('/Users/ganesathandavamponnuraj/Downloads/task17-test+keys/test/English/EnglishAW.test.xml')
    
    heads = tree.findall("//head")    
    
    for head in heads:
        print head.attrib," " + head.text
        
        
    
    