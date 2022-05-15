 #For any three lengths, there is a simple test to see if it is possible to form a
#triangle. If any of the three lengths is greater than the sum of the other two,
#then you cannot form a triangle. Otherwise, Enter three sides of a triangle,
#converts them to integers, and to check whether the given input lengths can
#form a triangle or not (Print : “Yes” or “No”).

#firstly input three numbers
a = int(input("Enter first length\n"))
b = int(input("Enter second length\n"))
c = int(input("Enter third length\n"))
#now check one by one that any of the three lengths is greater than the sum of the other two or not
if a+b<=c or a+c<=b or c+b<=a:
    print("No")
else:
    print("Yes") 
