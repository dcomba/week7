#!/usr/bin/env python

sequence=input("Enter a DNA sequence using ATGC syntax with no spaces: ")
sequence=sequence.upper()
#read user input of DNA sequence using ATGC syntax
Acount=0
Tcount=0
Gcount=0
Ccount=0
#sets counts 

for character in sequence:
	if character=="A":
		Acount=Acount+1
	elif character=="T":
		Tcount=Tcount+1
	elif character=="G":
		Gcount=Gcount+1
	elif character=="C":
		Ccount=Ccount+1

#calculates number of letter occurences

print("A:%d, T:%d, G:%d, C:%d" % (Acount,Tcount,Gcount,Ccount))
#prints values of letter occurences
