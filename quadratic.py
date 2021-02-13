import cmath

def quadratic(a,b,c):                                           
    print("The quadratic equation is: ",a,"x^2 +",b,"x +",c)   # printing the quadratic equation from a,b,c
    equation = (cmath.sqrt(b*b - 4*a*c))/(2*a)                 # formula of finding x values in quadratic equation
    x1 = -b + equation                                         # first value of x 
    x2 = -b - equation                                         # second value of x
    print("The values of x are: ",x1,x2)                       # printing x values...for quadratic equation, x has 2 values

a = int(input("Enter a value for 'a': "))                      #asking the inputs for a,b,c
b = int(input("Enter a value for 'b': "))
c = int(input("Enter a value for 'c': "))

quadratic(a,b,c)                                               # function call