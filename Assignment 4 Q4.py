#Question 4
#Halloween Candy
n=1
while n<200:
    if n%5==2 and n%6==3 and n%7==2:
        print("Number of candies in the box are",n)
        break
    else:
        n+=1
