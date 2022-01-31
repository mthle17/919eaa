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
def mix_texts(txt1, txt2):
    #return txt1 + " " + txt2 + " " + txt1
    return f"{txt1} {txt2} {txt1}"

txt1 = input("Please enter first text:")
txt2 = input("Please enter second text:")
out_txt = mix_texts(txt1, txt2)
out_txt = out_txt.title()
print(out_txt)
