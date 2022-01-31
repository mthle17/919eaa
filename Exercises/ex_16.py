"""
Create a function that returns environment variable of the name given by input parameter.
Then call the function with parameter 'UserProfile' and print out the returned value.
"""
import os

def print_env(name):
    res = os.environ[name]
    return res

home = print_env('UserProfile')
print(home)
