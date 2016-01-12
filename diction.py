# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:59:07 2015

@author: XuGang
"""
import re
import json

'''    
    ɑ :  \u0251
    æ:   \xe6
    ә :  \u04d9
    ʒ  :    \u0292
 ʃ   :  \u0283
 є    :   \u0454
 ʌ   :   \u028c
    ŋ   :   \u014b
    ɒ  :  \u0252
    ð  :  \xf0

'''    
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
    
    dictionary = {}    
    name = '.\dictionary\langwen1.txt'
    name1 = '.\dictionary\langwen_dict1.txt'
    
    fr = open(name,'r')  
    for line in open(name):  
        words_array = fr.readline().decode('utf-8').split("\t")
#        print  words_array[1]
#        value = replace(str(words_array[1]))
#        print re.sub(r"\\u0251",r"ɑ",words_array[1])
#        print words_array
#        if(len(words_array[0].split()) != 1):
#            dictionary[words_array[0]] = words_array[1]
        dictionary[words_array[0]] = words_array[1]
    fr.close()

#    jsonForm = [dictionary]
#    data_json = json.dumps(jsonForm)
    
    fw = open(name1,'w') 
    fw.write(str(dictionary))
    fw.close()

#    fw2 = open(name2,'w') 
#    fr1 = open(name1,'r') 
#    string = fr1.readline().encode('utf-8',"backslashreplace")
#    string_new = replace(string)
#    fw2.write(string_new)
#    fr1.close()
#    fw2.close()
#    finput = file(name2, 'r')    
#    dictionary = finput.read()    
#    dictionary = eval(dictionary)
#    finput.close()

   