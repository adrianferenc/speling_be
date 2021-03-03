#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:37:44 2021

@author: adrianferenc
"""

import random

my_file = open("words_alpha.txt", "r")
words = my_file.read()

word_list = words.split("\n")
my_file.close()


alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]

def initializer():
    full_list = random.sample(alphabet,7)
    center_letter = full_list.pop()
    return (full_list,center_letter)

class spellingBee:
    
    def __init__(self,letters,center_letter):
        self.letters=letters
        self.center_letter=center_letter
        self.score = 0
        self.words_found = 0
        self.found_words = list()
        self.hive = f'    {self.letters[1]}\n{self.letters[0]}       {self.letters[2]}\n    {self.center_letter}\n{self.letters[5]}       {self.letters[3]}\n    {self.letters[4]}\n'
    def solver(self):
        letter_set = set(self.letters+[self.center_letter])
        answers = list()
        for word in word_list:
            word_as_set = set(list(word))
            if word_as_set.issubset(letter_set) and self.center_letter in word_as_set and len(word)>=4:
                answers.append(word)
        answers.sort()
        return answers
    def scorer(word):
        if len(word)==4:
            return 1
        elif len(word)>=5:
            return len(word)

#print(initializer())
feb162021= spellingBee(['b','e','i','l','m','t'],'n')
feb172021 = spellingBee(['v','l','y','i','d','a'],'t')
feb182021 = spellingBee(['g','t','p','a','i','n'],'d')
feb192021 = spellingBee(['a','n','i','o','g','z'],'l')
feb202021 = spellingBee(['n','e','l','w','d','a'],'o')
feb212021 = spellingBee(['b','o','m','a','i','x'],'l')
feb242021 = spellingBee(['a','c','l','r','i','n'],'h')
feb262021 = spellingBee(['g','t','l','b','y','i'],'u')

#print(feb262021.solver())

