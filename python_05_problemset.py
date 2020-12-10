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

