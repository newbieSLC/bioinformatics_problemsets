#!/usr/bin/env python3

import sys

user_input=sys.argv[1]

#Create a script that has a if/else statement that:
#Tests to see if a number is positive or negative
#print "positive" if it is positive
#print "negative" if it is negative

#Add an elif to test if the number is equal to 0

#Add nested tests to see if:
#it is positive, in addition to printing "positive"
#test if it is smaller than 50
#if it is smaller than 50
#test if the number is even

#if it is smaller than 50 and even, print "it is an even number that is smaller than 50"
#if it is larger than 50, test if the number is divisible by 3
#if the number is larger than 50 and divisible by 3, print "it is larger than 50 and divisible by 3"

#In your previous nested loops, test the number 50. What prints to the screen? Is it the correct response?
#If not, you have a semantic error and need to alter your code to be correct with any number

#Do all the above but use sys.arg so that the value being tested comes from the command line
#Note that I have given that test value the name user_input and it will be sys.argv[1]

user_input=int(sys.argv[1])
if user_input > 0:
	print(user_input, "is positive.")
else:
	print(user_input, "is negative.")

user_input=int(sys.argv[1])
if user_input < 0:
  print('The number is a negative number')
elif user_input > 0:
  if user_input < 50:
    if user_input %2 == 0:
      print(user_input, '  is an even number smaller than 50')
    else:
      print(user_input, 'is a number less than 50 but is not an even number')
  elif user_input > 50:
    if user_input %3 == 0:
      print(user_input, 'is greater than 50 and divisible by 3')
    else:
      print(user_input, 'is greater than 50 but not divisible by 3')
print('End of test')








