#!/usr/bin/env python3

#make a function to calculate GC content in a given dna sequence

file_object=open('salDNA.txt', 'r')
dna=file_object.read()

def gc_content(dna):
  '''calculate the gc content of a DNA string'''
  dna_length=len(dna)
  g_content=dna.count('G')
  c_content=dna.count('C')
  gc_total=g_content + c_content
  gc_content=(gc_total/dna_length)
  return gc_content

#I can use for x in y to loop over a range
#Step indicates step length ie window range

step=2000

for start in range(0,len(dna),step):
  end=start+step
  subseq=dna[start:end]
  gccontent=gc_content(dna[start:end])
  print('From',start, end,' the GC content is:  ', gccontent)


# Take a slice at 10kb intervals and call up gc function
# This method is long and tedious

print('The length of the salDNA sequence is: ',len(dna))

slice1=dna[0:10001]
print('Slice 1 GC content is: ', gc_content(slice1))

slice2=dna[10000:20001]
print('Slice 2 GC content is: ', gc_content(slice2))

slice3=dna[20000:30001]
print('Slice 3 GC content is: ', gc_content(slice3))

slice4=dna[30000:40001]
print('Slice 4 GC content is: ', gc_content(slice4))
  
slice5=dna[40000:50001]
print('Slice 5 GC content is: ', gc_content(slice5))

slice6=dna[50000:60001]
print('Slice 6 GC content is: ',gc_content(slice6))

slice7=dna[60000:70001]
print('Slice 7 GC content is: ',gc_content(slice7))

slice8=dna[70000:80001]
print('Slice 8 GC content is: ',gc_content(slice8))

print('Slice 9 GC content is: ',gc_content(dna[80000:90001]))

print('Slice 10 GC content is: ',gc_content(dna[90000:100001]))

print('The overall GC content of salDNA is: ',gc_content(dna))

print('The GC content of salDNA from 40kb to 80kb is: ',gc_content(dna[40000:80000]))




















