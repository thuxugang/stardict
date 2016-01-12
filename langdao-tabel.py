# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:59:07 2015

@author: XuGang
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
    
if __name__ == "__main__":

    class word:
        def __init__(self,name,meaning_ch):
            self.name = name             
            self.meaning_ch = meaning_ch

    name = '.\dictionary\langdao_phrase_dict.txt'
    fr1 = open(name,'r') 
    string = fr1.readline()
    dict_words = eval(string)
    fr1.close()            
 
    
    array_words = sorted(dict_words.items(),key = lambda x:(x[0].lower()))  
    print "dict sorted..."
    
    name1 = "result.txt"
    fw = open(name1,'w') 
    
    for i in array_words:
        
#        print i[0]
        new_word = word(i[0],i[1]) 

        fw.write(new_word.name)
        fw.write("\t")
        fw.write(new_word.meaning_ch)                
            
    fw.close()
        
        
        
        
        
        
        
        
        
        
        
        