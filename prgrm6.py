list1= [6,8.3,9,5]
list2 = [1,9,7,5,0]
#check if the list have the same length
if len(list1) == len(list2):
    print("a. The list have the same length.")
else:
    print("a. The lists have diffrent lengths.")
#b check if the lists have same sum
    print(f"b.sum of list1:{sum(list1)} & sum of list2:{sum(list2)}")
if sum(list1) == sum(list2):
        print(" The lists sum to the same value.")
else:
    print(" The lists do not sum to the same value.")
    
#c. check if there are common values in both lists
    common_values = set(list1) & set(list2)
if common_values:
    print(f"c. common values in both lists:{common_values}")
else:
    print("c. There are no common values in both lists.")
