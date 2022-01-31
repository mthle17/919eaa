"""
Create a function that takes a sentence and returns a random word from that sentence.

*Example*
Please enter a sentence: Quick brown fox jumps over the lazy dog
Random word: brown
"""
import random

def get_random_word(sentence):
    words = sentence.split()
    word = random.choice(words)
    return word

sentence = input("Please enter a sentence: ")
random_word = get_random_word(sentence)
print(f"Random word: {random_word}")
