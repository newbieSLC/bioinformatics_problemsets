#!/usr/bin/env python3

#always remember to include the above on the first line to make it executable by python3
#if there are any modules to import, this would be the correct place to add import
#this assignment I don't have anything to import

#Python Problemset 2

myseq="GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA"

#Test to see if can find ATG in above seq
test1=myseq.find("ATG")
print(test1)


#Test to see if can find TTT in above seq
test2=myseq.find('TTT')
print(test2)


#write a script that assigns a value to a variable
#has a if/else statement which print out confirmation of truth if values is true
#it prints out not true if the value is not true

my_variable=2817
print ("My variable is ", my_variable)
print(my_variable < 1000)
 
if my_variable <1000:
  message1 = "true, my variable is less than 1000"
  print (message1)

else:
  print("false, my variable is greater than 1000")
  
#try another if/else
#this time the statement will be false

humanCHMP3="MGLFGKTQEKPPKELVNEWSLKIRKEMRVVDRQIRDIQREEEKVKRSVKDAAKKGQKDVCIVLAKEMIRSRKAVSKLYASKAHMNSVLMGMKNQLAVLRVAGSLQKSTEVMKAMQSLVKIPEIQATMRELSKEMMKAGIIEEMLEDTFESMDDQEEMEEEAEMEIDRILFEITAGALGKAPSKVTDALPEPEPPGAMAASEDEEEEEEALEAMQSRLATLRS"
print ("Human CHMP3 sequence is ", humanCHMP3)

if "MGLLV" in humanCHMP3:
  print ("MGLLV found")

else:
  print ("MGLF found, this is the parental copy")
  






   




