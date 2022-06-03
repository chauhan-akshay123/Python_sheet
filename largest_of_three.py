a = float(input('Please enter first number a : '))
b = float(input('Please enter second number b : '))
c = float(input('Pleasee enter third number c : '))

if(a>b and a>c):
    print("{0} is greater than both {1} and {2} ".format(a,b,c))
elif(b>a and b>c):
    print("{0} is greater than {1} and {2} ".format(b,a,c))
elif(c>a and c>b):
    print("{0} is greater than {1} and {2} ".format(c,a,b))
else:
    print("Either any two values or all the values are equal ")