#!/usr/bin/env python3
import sys

#remember to include command line parameters (arguments) and pass to the script

first_name=sys.argv[1]
first_color=sys.argv[2]
first_activity=sys.argv[3]
first_animal=sys.argv[4]
print(first_name, ' likes the color ', first_color, ' and the activity ' , first_activity, ' and the animal ' , first_animal)


name='diane'
if 'w' in name:
  message = ('I found the letter w')
  print(message)
elif 'z' in name:
  message = ('I found the letter z')
  print(message)
else:
  message = ('I did not find the letters w or z in diane')
  print(message)

user_import=int(sys.argv[5])
if user_import > 0:
  if user_import > 50:
    if user_import %3 == 0:
      print(user_import, ' is a positive number, is divisble by 3 and greater than 50')
    else:
      print(user_import, ' is a positive number, not divisible by 3 and greater than 50')
  elif user_import < 50:
    if user_import %2 == 0:
      print(user_import, ' is a positive number, is even and less than 50')
elif user_import == 0:
  print(user_import, ' is equal to zero')
else:
  print(user_import, ' is a negative number')
print("End of script.\n")


start=int(sys.argv[6])
end=int(sys.argv[7])+1

for item in range(start,end):
  print(item)

#now only print numbers that are even numbers and range is 1-100

for item in range(start,end):
  if item%2==0:
    print(item, ' is divisible by 2')
  elif item%3==0:
    print(item, ' is divisible by 3')
  else:
    print(item, 'is not divisble by 2 or 3')



