# pip install nltk
#download the nltk words using this command only once
# nltk.download('words')
# it outputs some meaningful words from characters which user inputs
import nltk
from itertools import permutations
from nltk.corpus import words
user=input("enter your anagrams:- ")
spel=[''.join(data) for data in permutations(user)]
for i in spel:
    if i in words.words():
        print(i)
