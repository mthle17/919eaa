"""
Create function that takes two arguments, each of them is a list of numbers.
list1 = [1,2,4,7,8]
list2 = [1,3,4,5,7,9]
Then it returns all numbers that are in list1, but not in list 2 (aka. difference list1 - list2).

*EXAMPLE*
{2, 8}
"""
def find_difference(list1, list2):
    res = set(list1).difference(list2)
    return res

list1 = [1,2,4,7,8]
list2 = [1,3,4,5,7,9]
difference = find_difference(list1, list2)
print(difference)
