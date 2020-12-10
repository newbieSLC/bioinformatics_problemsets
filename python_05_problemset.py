#!/usr/bin/env python3
import sys

#Write a script in which you construct a dictionary of your favorite things
favs={}
favs['book']='Pride and Prejudice'
favs['song']='Foo Fighters - Everlong'
favs['tree']='spruce'
print(favs)

#Print out your favorite book
print(favs['book'])


#Print out your favorite book but use a variable in the key
fav_book=favs['book']
print(fav_book)

#Print out your favorite song but use a variable in the key
fav_song=favs['song']
print('I made my favorite song a variable. My favorite song is ', fav_song)

#now print out fav tree
print(favs['tree'])

favs['organism']='dog'
fav_thing=favs['organism']
print(fav_thing)

#Take a value from the command line for fav_thing and print the value of that item from the dictionary

fav_thing=sys.argv[1]
print(sys.argv[1])


#Maybe you want to print out all the keys to the user so that they know what to pick from

name=input('Type "keys" and discover all the exciting keys in my dictionary named favs!!!  ')
for fav in favs:
  print(fav)


#Change the value of your favorite organism

favs['organism']='sasquatch'

fav_thing=sys.argv[2]
print(sys.argv[2])

#Use a for loop to print out each key and value of the dictionary
for fav in favs:
  item=favs[fav]
  print(fav,':', item)


#Make a set using the two different syntaxes for creating a set myset = set() and myset2 = {}
# What is the difference?
# Does it matter how you make it?

mySet = set('ATGTGGG')
mySet2 = {'ATGCCT'}

#To create an empty set you have to use set(), not {} the latter creates an empty dictionary
#So in the above example there is no difference
#But if we first created an empty set and wnanted to add to it, we must use set()

#Write a script to find the intersection, difference, union, and symetrical difference between these two sets

SetA ={'3','14','15','9','26','5','35','9'}
SetB ={'60','22','14','0','9'}

print('SetA: ', SetA, '\nSetB: ', SetB)
set_difference=SetA-SetB
print('The difference between SetA and SetB is ', set_difference)

set_intersection=SetA&SetB
print('The intersection of SetA and SetB is ', set_intersection)

set_union=SetA|SetB
print("The union of SetA and SetB is ", set_union)

set_symmetric=SetA^SetB
print('The symmetric difference between SetA and SetB is ', set_symmetric)













