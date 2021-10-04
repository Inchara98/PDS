word=input()
word1=''
for i in word:
    if(i.isupper())==True:
        word1+=(i.lower())
    elif(i.islower())==True:
        word1 += (i.lower())
    elif(i.isspace())==True:
        word1+=1
print(word1)

