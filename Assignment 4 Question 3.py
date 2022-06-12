#Question 3
#Multiplication game

import random
for i in range(1,11,1):
    m=random.randrange(1,10,1) #Generates a random value from 1 to 10
    n=random.randrange(1,10,1) #Generates a random value from 1 to 10
    ans=int(input((f"Question {i}: {m}*{n} = ")))
    if m*n==ans:
    # if the answer is correct print right and start the next iteration
        print("Right!")
        continue
    else:
    # if the answer is incorrect print wrong and start the next iteration
        print("Wrong. The answer is ",m*n)
        continue
