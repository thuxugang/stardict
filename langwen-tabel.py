# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:59:07 2015

@author: XuGang
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import re
import json
import wordnet
from bs4 import BeautifulSoup

def replace(string):
    
    string = re.sub(r"\\u0251",r"ɑ",string)
    string = re.sub(r"\\xe6",r"æ",string)
    string = re.sub(r"\\u04d9",r"ә",string)
    string = re.sub(r"\\u0292",r"ʒ",string)
    string = re.sub(r"\\u0283",r"ʃ",string)
    string = re.sub(r"\\u0454",r"є",string)
    string = re.sub(r"\\u028c",r"ʌ",string)
    string = re.sub(r"\\u014b",r"ŋ",string)
    string = re.sub(r"\\u0252",r"ɒ",string)
    string = re.sub(r"\\xf0",r"ð",string)

    return string
    
if __name__ == "__main__":

    class word:
        def __init__(self,name,synset,pron_en,pron_us,tag,meaning_en,meaning_ch,staccato):
            self.name = name             
            self.synset = synset 
            self.tag = tag 
            self.pron_en = pron_en 
            self.pron_us = pron_us 
            self.meaning_en = meaning_en
            self.meaning_ch = meaning_ch
            self.staccato = staccato

    name = '.\dictionary\langwen_dict.txt'
    fr1 = open(name,'r') 
    string = fr1.readline()
    dict_words = eval(string)
#    string_new = replace(string)
    fr1.close()            
 
#    wordnets = wordnet.getWordnet()
#    print "wordnets already..."
    
    array_words = sorted(dict_words.items(),key = lambda x:(x[0].lower()))  
    print "dict sorted..."
    
    name1 = "result.txt"
    fw = open(name1,'w') 

    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    
    for i in array_words:
        
#        if(str(i[0])[0] == "b"):
#            break        
#        
#        if(str(i[0])[0] != "a"):
#            continue
        print i[0]

        
        synset = ""
        staccato = ""
        pron_en = ""
        pron_us = ""
        prons = ""
        staccato = ""
        meanings_en = []
        meanings_ch = []
        related_phrase = []         
        
#        try:
#            synset = wordnets[i[0]]
#            
#        except:
#            pass
       
        text = i[1] 
        soup = BeautifulSoup(text,"lxml")
        iters = soup.stripped_strings
        
        k = 0
        pron_start = False
        meaning_start = False
        pron_count = 0
        meaning_count = 0
        meaning_en = ""
        meaning_ch = ""
        last = ""
        lasts = []
        tag = []
        tag_new = []
        
        maintag = ""
        
        for j in iters:
            
            k = k + 1

            if(k == 3):
                staccato = j
                
            if(j == r"/"):
                if(pron_count == 0):
                    pron_start = True
                    pron_count = 1
                else:
                    pron_start = False
            
            if(j in ["adjective","noun","adverb","verb","preposition","interjection","prefix","suffix","conjunction","pronoun","article"]):
                maintag = j
#                print j
                
            if(re.findall(r"^\d{1,2}\.$",j) != []):
                
                if(last in ["adjective","noun","adverb","verb","preposition","interjection","prefix","suffix","conjunction","pronoun","article"]):                   
                    tag.append(last)
                    tag_new.append(last)
                    
                elif(re.findall(r"\[.*\]", last) != []):
                    if(re.findall(r"\[.*\]", lasts[-2]) != []):
                        tag.append(str(maintag + lasts[-2] + last).strip())
                        tag_new.append(str(maintag + lasts[-2] + last).strip())
                    else:
                        tag.append(str(maintag + last).strip())
                        tag_new.append(str(maintag + last).strip())
                else:
                    try:
                        tag.append(tag[-1])
                        tag_new.append(tag[-1])
                    except:
                        tag.append(maintag)
                        tag_new.append(maintag)
#                print tag
                meaning_start = True
                meaning_en = ""
                meaning_ch = ""    
                
            if(pron_start):
                if(j != r"/"):
                    prons = prons + j
                continue
            
            if(meaning_start):
                if(re.findall(r"^\d{1,2}\.$",j) == []):                                  
                        
                    if(zhPattern.search(j) or j in ['(',')']):
                        meaning_ch = meaning_ch + j
                        meaning_start = False
                        
                        if(str(meaning_ch)[-1] == ":"):
                            meaning_ch = meaning_ch[:-1]
    
                        meanings_en.append(meaning_en.strip())
                        meanings_ch.append(meaning_ch.encode('utf-8'))
                        
                    else:
                        
#去掉词组                        
                        if(j.isupper()):
                            meaning_start = False
                            
                        elif((re.findall(r"\[.*\]", j) != [])):
                            tag_new[-1] = str(tag[-1] + j)

                        else:
                            meaning_en = meaning_en + " " + j
            
            last = j
            lasts.append(last)
           
#        print synset
        pron_en,pron_us = prons.split(';')[0],prons.split(';')[-1]
#        print staccato
#        print pron_en,pron_us
#        print meanings_en,meanings_ch
        new_word = word(i[0],synset,pron_en,pron_us,tag_new,meanings_en,meanings_ch,staccato) 
        
        string = ""
        m = 0
        for en in new_word.meaning_en:
            fw.write(new_word.name)
            fw.write("\t")
#            fw.write(str(new_word.synset))
#            fw.write("\t")
            fw.write(new_word.staccato)
            fw.write("\t")
            fw.write(new_word.pron_en)
            fw.write("\t")
            fw.write(new_word.pron_us)
            fw.write("\t")
            fw.write(tag_new[m])                
            fw.write("\t")
            fw.write(en)
            fw.write("\t")
            fw.write(meanings_ch[m])                
            fw.write("\n")
            m = m + 1

    fw.close()
        
        
        
        
        
        
        
        
        
        
        
        