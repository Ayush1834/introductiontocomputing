marks = int(input('enter your marks: '))
if marks < 25 and marks >=0:
    print("you have scored  F grade.")
elif marks >= 25 and marks <45:
    print("you have scored  E grade.")
elif marks >= 45 and marks <50:
    print("you have scored  D grade.")
elif marks >= 50 and marks <60:
    print("you have scored  C grade.")
elif marks >= 60 and marks <80:
    print("you have scored  B grade.")
elif marks >= 80 and marks <= 100:
    print("you have scored  A grade.")
else:
    print("please enter a valid marks !")
