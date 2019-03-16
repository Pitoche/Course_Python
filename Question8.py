# =================================
# created by Celeste quinlan 13-Mar-2019
# Course XXXX
# This program outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”
# QUESTION 8 
# =================================


from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%I:%M:%S") 

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)

modified_date_time = now.strftime("%A, %B %d""th " "%Y at ""%I"":%m%p")
print("date and time:",modified_date_time)


modified_date_time = now.strftime("%A, %B %d""th " "%Y at ""%H"":%m%p")
print("date and time:",modified_date_time)

