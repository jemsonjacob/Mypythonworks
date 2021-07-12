str=input("enter the string")
vowel=("a","e","i","o","u")
s=[]
for i in str:
    if i not in vowel:
        s.append(i)
print(s)