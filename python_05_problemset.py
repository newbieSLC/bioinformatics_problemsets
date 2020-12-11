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

#If you create a set using a DNA sequence, what will you get back?

dna_seq={'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC'}



#In python interpreter, I checked the class and it said:
#type(dna_seq)
#<class 'set'
#so the above DNA sequence is a set



#Nucleotide Composition. Write a script that:
#determines the unique characters in this sequence
#iterate over each unique character and count the number found in the sequence
#store each count in a dictionary.
#when you are done counting each character calculate and report the nucleotide composition and the GC content

dna='GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA'

#first create an empty dictionary

nt_count={}

#get a set of unique characters in our DNA string

unique=set(dna)
print('unique nt: ', unique)

#above variable unique, I made the dna sequence a set
#next, I printed out the characters. Since this is a set, it will automatically print out only the unique characters
#and in a dna sequence those characters will be A, T, G, C and possibly N

#now iterate through each nucleotide
#next, count the number of the unique nt in dna
#then add the count to our dictionary

for nt in unique:
  count=dna.count(nt)
  nt_count[nt]=count
print('nt count: ', nt_count)

#now calculate and report the nucleotide composition and the GC content

dna_length=len(dna)
print('The length of the dna sequence is ', dna_length)

GC_sum=nt_count['G']+nt_count['C']
print('The sum of G+C is ', GC_sum)

GC_percent=(GC_sum/dna_length)*100
print('The percent GC in the dna sequence is ', GC_percent, '%')














