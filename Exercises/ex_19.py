"""
Create program that prints out current date and time values.

*EXAMPLE*
Current date: 18.01.2022
Current time: 09:59:48
"""
from datetime import datetime

now_str = datetime.now()
date_str = now_str.strftime("%d.%m.%Y")
time_str = now_str.strftime("%H:%M:%S")

print(f"Current date: {date_str}")
print(f"Current time: {time_str}")
