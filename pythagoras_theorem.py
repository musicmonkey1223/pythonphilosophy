import math                                                 # Importing math library for sqrt function
side1 = int(input("Enter the 1st side of a Triangle:  "))   # Taking input for side1
side2 = int(input("Enter the 2nd side of a Triangle:  "))   # Taking input for side2

Hypotenuse_square = (side1*side1) + (side2*side2)           # Hypotenuse_square = side_square + side_square
Hypotenuse = math.sqrt(Hypotenuse_square)                   # Hypotenuse  = squareroot of side_square + side_square
print(Hypotenuse)                                           # Printing the Hypotenuse