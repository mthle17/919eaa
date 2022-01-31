"""
Write a program that takes two date values and calculates difference in days.
When program is run, user must enter the two dates.
After dates are parsed, difference in days is calculated and printed out.

*EXAMPLE*
Please enter a date in 'yyyy-MM-dd' form (e.g. 2022-01-25): 2022-01-10
Please enter a date in 'yyyy-MM-dd' form (e.g. 2022-01-25): 2022-01-30
Difference in days: 20
"""
from dateutil import parser

date1_str = input("Please enter date 1 in 'yyyy-MM-dd' form (e.g. 2022-01-25): ")
date2_str = input("Please enter date 2 in 'yyyy-MM-dd' form (e.g. 2022-01-25): ")

date1 = parser.parse(date1_str)
date2 = parser.parse(date2_str)
diff = date2 - date1

print(f"Difference in days: {diff.days}")
