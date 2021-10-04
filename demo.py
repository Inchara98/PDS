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


a = "inchara"
print(a.upper())


n=input("")
for i in n:
    n=chr(ord(i)-(-32))
    print(n,end='')

varLowerCase = "INCHARA"
print(varLowerCase.lower())

