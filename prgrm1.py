#get input from the user
year1 = int(input("Enter the starting year:"))
year2 = int(input("Enter the ending year:"))
print(f"leap years from {year1} to {year2}:")
#leap year -if the year is visible by 4,and either not divisible by 100 or divisible by 400
for year in range(year1,year2+1):#to itrate through each year from year1 to year2
    if year % 4 == 0 and (year % 100 !=0 or year % 400 == 0):
        print(year)
