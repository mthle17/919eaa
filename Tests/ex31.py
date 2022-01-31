continue_=True
liste=[]
while continue_:
    entry=input("please enter a number : ")
    entry=entry.strip()
    try:
        liste.append(int(entry))
    except:
        continue_=False
sum=0
for element in liste:
    sum+=element
print (liste, list(set(liste)), sum)