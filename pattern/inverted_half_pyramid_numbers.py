#! /usr/bin/python3

number = int(input("enter a number"))

for i in range(number,0,-1):
	for j in range(i):
		print(j,end=(""))
	print("")


'''
012345
01234
0123
012
01
0

'''