"""
Create a function that takes a sentence, converts it to lowercase and 
returns the shortest and the longest word from the sentence. Function 
should remove characters ',' and '.' from words.
Use tuple for return value.

When program is run, user must enter the sentence and the function gets called.
Then the program writes out the longest and the shortest word.

HINT: you can use special "key" parameter of the min/max functions:
    e.g. min(some_word_list, key=len)

*Example*
Please enter a sentence: Quick, brown fox IS Jumping, over the Lazy Dog.
Long one: jumping
Short one: is
"""
def long_short(sentence):
    words = sentence.split()
    for idx, word in enumerate(words):
        words[idx] = word.lower().replace(',', '').replace('.', '')

    longest = max(words, key=len)
    shortest = min(words, key=len)
    return (longest, shortest)

text = input("Please enter a sentence: ")
long, short = long_short(text)
print(f"Long one: {long}")
print(f"Short one: {short}")
