#Question no 6
a=int(input("Enter the input"))
b=int(input("Enter the input"))
num=a^b
Count_flipped_bit=0
while(num !=0):
num=num&(num-1)
Count_flipped_bit +=1
print("Number of bits needed to be flipped to covert a to b is:",Count_flipped_bit)
