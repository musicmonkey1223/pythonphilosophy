number = int(input("Enter the number to find fibonacci series:  "))   # Taking input from user

count = 0                                             
n1 = 0
n2 = 1

if number == 1:                                                     #if number is equals to 1, "fibonacci series is 0" will be printed
    print("Fibonacci series of 1 is 0")
elif number <= 0:                                                  #if number is lessthan or equal to zero, "Enter only Natural numbers" will be printed
    print("Enter only Natural numbers")
else:
    while count < number:                                          #n1 and n2 will be added and result is stored in nth 
        print(n1)                                                  #n1 will be printed each time
        nth = n1 + n2                                              #count will be incremented 
        n1 = n2                                                    #if count is equal to number it stops
        n2 = nth
        count+=1