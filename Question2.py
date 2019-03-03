# =================================
# created by Celeste quinlan 18-Feb-2019
# Course XXXX
# This program outputs whether or not today is a day that begins with the letter T.
# QUESTION 2 
# =================================

import datetime                                                     # Importing datatime Pythoin module
now = datetime.datetime.now()                                       # setting var for todays day (ineteger)
weekday = datetime.datetime.today().strftime('%A')                  # Setting weekday (string)
if datetime.datetime.today().weekday() == 1:                        # evaluating to todays '
    	print("Yes! It is Tuesday")         #  Printing out if Tuesday
elif datetime.datetime.today().weekday() == 3 :
		print("Yes! It is Thursday")         #  Printing out if Tursday
else:                                       
		print("Unfortunately today is not either Tuesday nor Thursday."'\n'"Today is:", weekday)  #esle printing out message and weekday string

#angel comment for github

 