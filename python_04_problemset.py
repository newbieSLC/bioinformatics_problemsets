#!/usr/bin/env python3
import sys

# above makes it executable
# any imports go next

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
species_split= sorted(species)
print("Now I will sort the list alphabetically")
print(species_split)
#sort the list by length of each string and print, shortest string first
print("Now I'll sort the list by shortest length first")
print(sorted(species_split, key=len))


#Write a script that uses a while loop to calculate the factorial of 1000
x = 1
factorial = 1
while x < 1000:
	x += 1
	factorial *= x 
print(factorial)

#Iterate through each element of this list using a for loop: [101,2,15,22,95,33,2,27,72,15,52]

elements=[101,2,15,22,95,33,2,27,72,15,52]
for element in iter( elements):
  if element%2==0:
    print(element)



elements= [101,2,15,22,95,33,2,27,72,15,52]
#Sort the elements of the above list
elements_sorted=sorted(elements)
print("Here are the elements sorted")
print(elements_sorted)

#Calculate two cumulative sums, one of all the even values - and one of all the odd values
#Print only the final two sums

even_sum=0
odd_sum=0

for element in elements_sorted:
  print(element)
  if element%2 == 0:
    even_sum += element
  else:
    odd_sum += element

print("Sum of even numbers is " + str(even_sum))
print("Sum of odd numbers is " + str(odd_sum))

 
#Write a script that uses range() in a for loop to print out every number between 0 and 99
#Remember the strange way python counts and prints numbers

for item in range(0,100):
  print(item)

#Modify your loop to print out every number between 1 and 100

for item in range(0,101):
  print(item)

#Create a new script that uses list comprehension to print out every number between 1 and 100
print("Now print out the same using list comprehension")
[print(item) for item in range(0,101)]

#Write a new script that takes the start and end values from the command line
print("Give the script start and end values from the command line")
start=int(sys.argv[1])
end=int(sys.argv[2])+1
[print (item) for item in range(start,end)]

print("Give the script start and end values from the command line")

#my first loop

for name in diane_list:
  print(name + " is a family member")
  name_length=len(name)
  print(name + " is a family member whose name has " +  str(name_length) + " letters")

#iterate over a single word

name=("python")
for character in name:
  print(character + " is a letter in python")


