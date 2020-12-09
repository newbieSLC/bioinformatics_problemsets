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



