# =================================
# created by Celeste quinlan 13-Mar-2019
# Course XXXX
# This program  takes a positive ﬂoating point number as input and outputs an approximation of its square root
# QUESTION 7 
# =================================


import math

user_input = input ("Enter  your floating positive number bigger than 0: \n")
try:
    val = float(user_input)
    if(val > 0):
        print("Yes, input string is a float number.")
        root_square = round(math.sqrt( val ),2)
        print("The Square root of this number, rounded to two decimals is : ", root_square)
    elif (val == 0):
        print("please enter a  float number  floating positive number bigger than 0. Bye")
    else:
       print("User number is negative . Bye")
except ValueError:
   print("That's not an float!")
   print("No.. input string is not a float number. It's a string. Bye")



