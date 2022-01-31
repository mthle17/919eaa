"""
Write a program that takes two time values and calculates difference in seconds.
When program is run, user must enter the two time values.
After time values are parsed, difference in seconds is calculated and printed out.

*EXAMPLE*
Please enter time in 'hh:mm:ss' form (e.g. 23:59:59): 12:34:56   
Please enter time in 'hh:mm:ss' form (e.g. 23:59:59): 14:34:56 
Difference in seconds: 7200.0
"""
from dateutil import parser

time1_str = input("Please enter time 1 in 'hh:mm:ss' form (e.g. 23:59:59): ")
time2_str = input("Please enter time 2 in 'hh:mm:ss' form (e.g. 23:59:59): ")

time1 = parser.parse(time1_str)
time2 = parser.parse(time2_str)
diff = time2 - time1

print(f"Difference in seconds: {diff.total_seconds()}")
