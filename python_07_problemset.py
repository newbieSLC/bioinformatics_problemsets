#!/usr/bin/env python3

#import regular expression module
import re

#Problem #1 In the file Python_07_nobody.txt find every occurrence of 'Nobody' and print out the position

nobody_file=open('Python_07_nobody.txt', 'r')

counter =1
for line in nobody_file:
  for match in re.finditer(r'Nobody', line):
    start=match.start()+1
    end=match.end()
    counter += 1
    print("Line: {}  starts at:{}  ends at:{}".format(counter,start,end))
print("Done")

#Problem #2
#substitute every occurrence of 'Nobody' with your favorite name
#write an output file with that person's name

with open('Python_07_nobody.txt') as nobody_file:
  for line in nobody_file:
    line=line.rstrip()
    line=re.sub(r"Nobody","Diane", line)
    print(line)

#Problem 3
#Using pattern matching, find all the header lines in Python_07.fasta
#Every Fasta entry starts with '>'

with open('Python_07.fasta') as FO:
  for line in FO:
    if re.search(r">", line):
      print(line.rstrip())

#Problem #4
#If a line matches the format of a FASTA header, extract the sequence name and description using sub patterns
#Print lines something like this id:"extracted seq name" desc:"extracted description"

with open('Python_07.fasta') as FO:
  for line in FO:
    line=line.rstrip()
    if re.search(r'^>', line):
      for found in re.finditer(r'^>(\S*)? (.*)$', line):
        ID = found.group(1)
        Descrip=found.group(2)
  print('ID: ', ID, 'Description: ', Descrip)

#Problem #5
#Create a FASTA parser, or modify your FASTA parser from the previous problem set, to use regular expressions
#Also make sure your parser can deal with a sequence that is split over many lines

seqdict = {}

with open('Python_07.fasta') as FO:
    seq = ''
    for line in FO:
        line = line.rstrip()
        if re.search(r"^>", line):
            header = line
            seq = ''
        else:
            seq += line
            seqdict[header] = seq
seqdict[header] = seq
print (seqdict)

#Problem #6
#The enzyme ApoI has a restriction site: R^AATTY where R and Y are degenerate nucleotideides
#Write a regular expression to find and print all occurrences
#R= A or G
#Y=C or T 

with open ('Python_07_Apo1.fasta') as FO:
  for line in FO:
    seq += line
  for match in re.finditer(r'[A|G]A{2}T{2}[C|T]', seq):
     print(match)


# Problem 7

#Determine the site(s) of the physical cut(s) by ApoI in the sequence
#Print out the sequence with "^" at the cut site

  
seq = ''

with open("Python_07_Apo1.fasta") as FH:
    for line in FH:
        seq += line

newseq = re.sub(r"([A|G])(AATT[C|T])",r"\1^\2",seq)
print (newseq)

# Problem 8
#determine the lengths of your fragments and sort them by length
#hint: convert the string into a list
#I'm thinking I should use split to split a string into a list on the delimiter ^
# get the lengths of the fragments with a list comprehension



frag_list = newseq.split("^")
for frag in frag_list:
  length=len(frag)
  print('The fragment length is ', length, '\nand the fragment is: ', frag)













                  
















