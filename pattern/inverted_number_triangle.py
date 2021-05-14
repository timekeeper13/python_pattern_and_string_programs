#!/usr/bin/python3

def inverted(size):
	for i in range(1,size):
		for j in range(i,size):
			print(i,end=(""))
		print("")

size = int(input("enter number : "))

inverted(size)



'''
pattern:

11111
2222
333
44
5


'''