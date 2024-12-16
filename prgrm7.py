s=input("Enter a word:")
c=s[0]#it extract the first charector of the input word
str1=s.replace(s[0],'$')
print(c+str1[1:])
