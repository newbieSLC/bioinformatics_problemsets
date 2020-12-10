#!/usr/bin/env python3


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




