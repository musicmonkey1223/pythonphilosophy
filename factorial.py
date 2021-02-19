print("Let's do Factorial")                                      #printing the operation what we are performing

def factorial(number):                                            #defining the factorial method
    result = 1                            # result is intially defined with 1. if we define initially with 0 the factorial will be 0.
    if number == 0:                                              # if number is equals to 0, it prints 1.
        print("The factorial of 0 is 1")
    elif number < 0:                                             # if number is negative number , it prints error message
        print("Error..Enter only whole numbers")
    else:               
        for i in range(1, number+1):                             # we are using range function for multiplication of numbers 
            result = result * i                         # multiplication of numbers is factorial. result is stored in result variable
        print("The Factorial of" ,number, "is : ", result)       # result will be printed


number = int(input("Enter the number: "))                        # Input is taken from user
factorial(number)                                                # Function is called