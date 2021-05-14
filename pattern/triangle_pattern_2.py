#!/usr/bin/python3

def pattern(size):
	for i in range(1,size+1):
		for j in range(1,i+1):
			print(j,end=(""))
		print("")

size=int(input("enter number : "))

pattern(size)


'''
pattern:

1
12
123
1234
12345


'''