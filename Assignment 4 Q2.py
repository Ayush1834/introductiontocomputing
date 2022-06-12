year = int(input("enter the year: "))
if year % 4 == 0 and year % 100 !=0:
    print("The year is a leap year")
elif year%4==0 and year%100==0 and year%400==0:
    print("the year is a leap year")
else: 
    print("not a leap year")
