i#!/usr/bin/env python3

# above makes it executable
# any imports should go next
# no imports on this script

#this script is for practicing Python lists and loops

#this is a list. a LIST is surrounded by brackets, separated by commas

diane_list = ['Paul', 'Diane', 'Annie', 'Zoe', 'Ollie']
print('The family members of Diane are ' + str(diane_list))

#retrive a single value in list

diane_list[2]
print("The third name on the list is " + diane_list[2])

#replace Annie with a different name, use Anniebelle

diane_list[2]='Anniebelle'
print("The third name on the list is now " + diane_list[2])

#append list to add a new element to the end
diane_list.append('Tristan')
print("I will now add Tristan to the end of the list")
print(diane_list)

#use insert to add a new element to the beginning
diane_list.insert(0, "Lucy")
print("I will now add Lucy to the beginning of the list")
print(diane_list)

#add a new element somewhere other than the beginning or the end
diane_list.insert(3, "Noel")
print("I will now add Noel to the middle of the list")
print(diane_list)


#remove an element using pop.pop removes and returns the last value in the list
diane_list.pop()
print("I have removed the last element in the list. The last element is " + diane_list.pop())
print(diane_list)

#remove an element from the beginning. use remove
diane_list.remove("Lucy")
print("I have removed the name Lucy from the list")
print(diane_list)

#remove an element from somewhere in the middle of the list
diane_list.remove("Paul")
print("I have removed Paul from the list")
print(diane_list)

#use join to create a string from your list)
#define a separator
separator=(', ')
print(separator.join(diane_list))
print('In the above list notice how I used the join method to create a string from my list')

#splitting a string to make a loop
#split take a single argument, called delimiter, and splits the original string wherever it sees the delimiter
#and in doing so produces a list
#here's a string

taxa = ("sapeins, erectus, neanderthalensis")
print(type(taxa))
print ("This is a string named " + taxa)
print(taxa[1])

#now we split the string and make it a list. notice the brackets, indicating it's now a LIST
#to print some text string with our new list, we have to use the str function

species=taxa.split(",")
print(type(species))
print("This is now a list " + str(species))
print(species[1])

#sort the list alphabetically
speciessort=sorted(species["erectus", "neanderthalensis", "sapiens"])
print(speciessort)




#my first loop

for name in diane_list:
  print(name + " is a family member")
  name_length=len(name)
  print(name + " is a family member whose name has " +  str(name_length) + " letters")

#iterate over a single word

name=("python")
for character in name:
  print(character + " is a letter in python")


