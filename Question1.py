# =================================
# created by Celeste quinlan 18-Feb-2019
# Course XXXX
# This program asks the user to input any positive integer and outputs the sum of all numbers between one and that number.
# QUESTION 1 
# =================================

selectedNumber=input('Please enter your selected number : ')   	# Reading number from keyboard
number = int(selectedNumber)									# Casting string to integer and store as new int var
total = 0														# Sum counter
while number > 0 :												# start loop from slected number to > 0
	total = number + total										# Adding values to teh total
	number -= 1     											# Decreasing counter by 1 in each iteration
print("The sum of integers from your number down is: ", total)  # Printint message  and result total  
#angel comment for github