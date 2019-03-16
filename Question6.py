# =================================
# created by Celeste quinlan 13-Mar-2019
# Course XXXX
# This program  takes a user input string and outputs every second word..
# QUESTION 6 
# =================================

import re  # Import module re to work with strings 

user_sentence = input("Please neter your sentence \n")       #String input from user
## Removing all unnecessary whitespaces start, end and duplicates 
user_sentence = user_sentence.strip()                       # Removing training spaces begining and end
user_sentence = re.sub(' +', ' ',user_sentence)              #Remvoving duplicat white espaces
print ("Remvoing intial spaces ==>:", user_sentence.strip()) #Re-Printing string without unnecsaary spaces 

#### Now we have a "clean srring to work with

large = len(user_sentence.split())                             #using len function to get length of string in number of words
senteced_splitted = user_sentence.split(" ")                   #splitted string into words
words = user_sentence.split("\\")
print ("The number of words of this sentence is ; ", large)    #simply prints out length of string as number of words

i = 0

#for i in range(0,len(senteced_splitted)):                        #start of fopr loop to length
#    if i % 2 != 0:                                             #
#      print("Word in position ",i,"in teh string is : ",senteced_splitted[i])                              #print splitted string 

while i <= len(senteced_splitted) :
      if i % 2 != 0:  
        print("Word in position ",i,"in teh string is : ",senteced_splitted[i])  
      else :
          print("Word in position ",i)
      
      i += 1
