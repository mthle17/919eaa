"""
Create function that takes two arguments, each of them is a list of numbers.
list1 = [1,2,4,7,8]
list2 = [1,3,4,5,7,9]
Then it returns all numbers that are both in list1 and list 2 (aka. union).

*EXAMPLE*
{1, 2, 3, 4, 5, 7, 8, 9}
"""
def find_union(list1, list2):
    res = set(list1).union(list2)
    return res

list1 = [1,2,4,7,8]
list2 = [1,3,4,5,7,9]
union = find_union(list1, list2)
print(union)
