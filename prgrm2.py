List1=[2,4,-4,-6,8,5]
List2=[i for i in List1 if(i>0)];
print(f"positive list ={List2}")

List3= [i**2 for i in List2]
print(List3)

word=input("Enter a word:")
listvowels=[i for i in word if i in "aeiouAEIOU"]
print(f"vowels are {listvowels}")

w=input("Enter any Charecter:")
odval=[ord(i) for i in w]
print(odval)
