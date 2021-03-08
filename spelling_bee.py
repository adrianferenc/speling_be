#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:37:44 2021

@author: adrianferenc
"""

import random
import tkinter as tk

my_file = open("words_alpha.txt", "r")
words = my_file.read()

word_list = words.split("\n")
my_file.close()


alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]



class spellingBee:
    
    def __init__(self):
        self.full_list = self.initializer()
        self.letters = self.full_list[0:6]
        self.center_letter=self.full_list[-1]
        self.score = 0
        self.words_found = 0
        self.found_words = list()
    def initializer(self):
        self.full_list = random.sample(alphabet,7)
        while not self.pangrammer()[0]:
            self.full_list = random.sample(alphabet,7)
        return self.full_list
    def solver(self):
        center_letter = self.full_list[-1]
        letter_set = set(self.full_list)
        answers = list()
        for word in word_list:
            word_as_set = set(list(word))
            if word_as_set.issubset(letter_set) and center_letter in word_as_set and len(word)>=4:
                answers.append(word)
        answers.sort()
        return answers
    def scorer(self,word):
        if len(word)==4:
            return 1
        elif len(word)>=5:
            return len(word)
    def pangrammer(self):
        is_there_a_pangram=False
        pangrams = list()
        for word in self.solver():
            if len(set(list(word)))==7:
                is_there_a_pangram=True
                pangrams.append(word)
        return [is_there_a_pangram,pangrams]

game = spellingBee()
       
 
root = tk.Tk()
root.title('Speling Be')
hive = tk.Frame(root)
hive.grid(row=0,column=0)
words = tk.Frame(root)
words.grid(row=0,column=1)
guess = tk.Frame(root)
guess.grid(row=1, column=0, columnspan=2)
guess.grid_forget()

clicker_name = 'Press to start'

def clicker():
    (letters,center_letter) = (game.letters,game.center_letter)
    random.shuffle(game.letters)
    mylabel1 = tk.Label(hive, text=letters[0])
    mylabel1.grid(row=0,column=1)
    mylabel2 = tk.Label(hive, text=letters[1])
    mylabel2.grid(row=1,column=0)
    mylabel3 = tk.Label(hive, text=letters[2])
    mylabel3.grid(row=1,column=2)
    mylabel4 = tk.Label(hive, text=letters[3])
    mylabel4.grid(row=3,column=0)
    mylabel5 = tk.Label(hive, text=letters[4])
    mylabel5.grid(row=3,column=2)
    mylabel5 = tk.Label(hive, text=letters[5])
    mylabel5.grid(row=4,column=1)
    center = tk.Label(hive, text=center_letter)
    center.grid(row=2,column=1)
    mybutton["text"] = 'Shuffle'
    guess.grid(row=1, column=0, columnspan=2)
    guess_button.grid(row=0,column=2)
    
  
guesslabel = tk.Label(guess, text="Guess your word:")
guesslabel.grid(row=0,column=0)
enter = tk.Entry(guess)
enter.grid(row=0,column=1)
enter.focus_set()
word_alert = tk.Label(words, text='')
word_alert.grid(row=0)
def guesser(event=None):
    guessed = enter.get()
    if guessed in game.solver() and guessed not in game.found_words:
        game.words_found+=1
        game.found_words.append(guessed)
        game.score +=game.scorer(guessed)
        if guessed in game.pangrammer()[1]:
            word_alert["text"] = 'You found a pangram!'
        else:
            word_alert["text"] = ''
    elif guessed in game.found_words:
        word_alert["text"] = 'You already guessed that word!'
    else:
        word_alert["text"] = 'That isn\'t a valid word'

    words_found_label = tk.Label(words, text='Words found: '+ str(game.words_found))
    words_found_label.grid(row=1)
    words_list_label = tk.Label(words, text=', '.join(game.found_words))
    words_list_label.grid(row=2)
    score_label = tk.Label(words, text='Score: '+ str(game.score))
    score_label.grid(row=3)
    enter.delete(0, 'end')
    enter.insert(0, "")
    
mybutton = tk.Button(hive, text = clicker_name, padx = 100, pady = 30, command = clicker)
mybutton.grid(row=5,column=0, columnspan=3)



guess_button = tk.Button(guess, text = 'Guess', command = guesser)
guess_button.grid(row=1,column=0,columnspan=2)
root.bind('<Return>', guesser)
guess_button.grid_forget()

print(game.pangrammer())
print(game.solver())
root.mainloop()





