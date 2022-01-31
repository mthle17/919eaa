"""
Create function that concatenates two text variables in a specific way.
If text variables are "text1" and "text2", result should look like:
    "text1 text2 text1"
When program is run, it should ask for text variables and call the function.
Print the result.

*Example*
Please enter first text: aaa
Please enter second text: bbb
aaa bbb aaa
"""
def concat3(str1, str2):
    return str1 + " " + str2 + " " + str1

str1 = input("Please enter first text: ")
str2 = input("Please enter second text: ")
concat_result = concat3(str1, str2)
print(concat_result)
