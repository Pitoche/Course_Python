
# =================================
# created by Celeste quinlan 18-Feb-2019
# Course XXXX
# This program asks the user to input any positive integer and outputs the successive values of the following calculation. 
#       At each step calculate the next value by taking the current value and, 
#       if it is even, divide it by two, 
#       but if it is odd, multiply it by three and add one. 
#       Have the program end if the current value is one
# QUESTION 4 
# =================================


selectedNumber=input('Please enter a positive integer number : ')   	# Reading number from keyboard
number = int(selectedNumber)					# Casting string to integer 
    
if(number > 0):
    print("User number is positive ==>", selectedNumber)
    if (number == 1):
        print("please use a Number bigger than 1 to start operations")
else:
    print("User number is negative ")
while (number > 0) and (number != 1) :
    if number % 2  == 0 :
        print ("Before operating on number is: ", number)
        number = number / 2
        print ("Is EVEN.So, divided by 2 is ", number)
    else :
        print ("Before operating on number is: ", number)
        number = (number * 3 ) +1
        print ("Is ODD. So, multiplied by 3 and added 1 is: ", number)

    print ("Now we have reduced thsi number to 1 : ", number)