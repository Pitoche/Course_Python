# =================================
# created by Celeste quinlan 18-Feb-2019
# Course XXXX
# This program prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.
# QUESTION 3 
# =================================

print("start here ")
initialNumber = 1000                            # Initial number used 
finalNumber = 10000                             # Final number usedf 
counter = initialNumber                        # Counter for iteractions 


print("Initial Number: ", initialNumber)        # checking values in the Front end for var initialNumber 
print("finalNumber: ", finalNumber)             # checking values in the Front end for var finalNumber 
print("Counter : ",counter)
while counter <= finalNumber :                  # Start loop from Initial to final
    if counter%6 == 0  and counter%12 != 0:     # Checking for numbers divisible by 6 NOT divisible by 12
        print (counter)                         # Printing numbers div by 6 and not by 12
    counter += 1                                # incrementting counter with each loop 
