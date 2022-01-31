
input1=input("Please enter time in 'hh:mm:ss' form (e.g. 23:59:59): ")
input2=input("Please enter time in 'hh:mm:ss' form (e.g. 23:59:59): ")

splitted_1=input1.split(":")
splitted_2=input2.split(":")

difference=0
difference+=(int(splitted_1[0])-int(splitted_2[0]))*3600
difference+=(int(splitted_1[1])-int(splitted_2[1]))*60
difference+=int(splitted_1[2])-int(splitted_2[2])

print("Difference in seconds is :", abs(difference))