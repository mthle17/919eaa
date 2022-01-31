"""
Create a function that takes a list and for each item writes out an index and 
the item itself.

*Example*
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
...
0: Monday
1: Tuesday
2: Wednesday
3: Thursday
4: Friday
5: Saturday
6: Sunday
"""
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for index, day in enumerate(days):
    num = index + 1
    print(f"{num}: {day}")
