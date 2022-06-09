a = int(input('enter a number: '))
print('+,-,x,/,exp')
n = input()
b = int(input('enter another number: '))
if n =='+':
    print(a+b)
elif n == '-':
    print(a-b)
elif n == 'x':
    print(a*b)
elif n == '/':
    print(a/b)
elif n == 'exp':
    print(a ** b)
else:
    print('please enter a valid operation')
