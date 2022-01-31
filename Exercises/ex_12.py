"""
Create a function that takes a sentence and returns list of all distinct words.
Call the function and print out the result in the reverse alphabetical order.

When program is run, user must enter the sentence the function gets called.

*Example*
Please enter a sentence: if it is it it is it
['it', 'is', 'if']

*Example*
Please enter a sentence: Quick brown fox jumps over the lazy dog
['the', 'over', 'lazy', 'jumps', 'fox', 'dog', 'brown', 'Quick']
"""
from audioop import reverse


def distinct_words(sentence):
    words = sentence.split()
    return list(set(words))

sentence = input("Please enter a sentence: ")
words = distinct_words(sentence)
words.sort()
words.reverse()
print(words)
