"""
Create function that takes two arguments, each of them is a list of numbers.
list1 = [1,2,4,7,8]
list2 = [1,3,4,5,7,9]
Then it returns all numbers that are in both lists (aka. intersection).

*EXAMPLE*
{1, 4, 7}
"""
def find_intersection(list1, list2):
    res = set(list1).intersection(list2)
    return res

list1 = [1,2,4,7,8]
list2 = [1,3,4,5,7,9]
intersection = find_intersection(list1, list2)
print(intersection)
