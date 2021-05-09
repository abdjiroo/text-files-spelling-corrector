# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 00:15:12 2020

@author: abdullah
"""
import re
from collections import Counter

def words(text): return re.findall(r'\w+', text.lower())
WORDS = Counter(words(open('corpus.txt').read()))
def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)
def known(words): return list(w for w in words if w in WORDS)
def find(word):
    fre=[]
    test=known(edits1(word))
    for i in range(len(test)):
        fre.append(WORDS[test[i]])
    if not fre:
        return " "
    else:
        ma=max(fre)
        index=fre.index(ma)
        return test[index]
raw=words(open('/add_file_name/.txt').read())      


correct=[]
for i in range(len(raw)):
    correct.append(find(raw[i]))

f = open("words_correct.txt", "w")
for ele in correct:
    f.write(ele+'\n')

f.close()
