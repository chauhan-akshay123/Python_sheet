a = float(input('Please enter first number a : '))
b = float(input('Please enter second number b : '))

if(a>b):
    print("{0} is greater than {1}".format(a,b))
elif(b>a):
    print("{0} is greater than {1} ".format(b,a))
else:
    print("Both a and b are Equal ")