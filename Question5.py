# =================================
# created by Celeste quinlan 03-MAR-2019
# Course XXXX
# This program asks the user to input a positive integer and tells the user whether or not the number is a prime.
# QUESTION 5 
# =================================
user_number = input ("Please enter your number: ==> ")    # User input number
#number = int(user_number)                                 # casting from String to Integer
try:
    number = int(user_number)
    if (number < 0):
       print("Entered User number is negative. Cannot continue. Bye! ")
       
    elif (number == 1):
       print("User number is positive. However we need an integer bigger than 1 in order to start processing")
       
    elif (number == 0) :
        print("Please use a Number bigger than 1 to start operations. Cannot continue. Bye!")
        
    elif (number > 1) :
        print("Validated number",user_number)
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
    else:
        print(number, "is not a prime number")

 
except ValueError:
    print("No.. input string is not a number. It's a string. PLEASE TRY AGAIN!!!")
    
#if number > 1:
   