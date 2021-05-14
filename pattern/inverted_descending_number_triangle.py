#!/usr/bin/python3

def inverted(size):
	for i in range(size,0,-1):
		for k in range(i)	:
			print(i,end=(""))
		print("")

size = int(input("enter number  : "))

inverted(size)


'''
55555
4444
333
22
1

'''
