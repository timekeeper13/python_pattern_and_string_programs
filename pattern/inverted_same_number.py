#! /usr/bin/python3

number= input("input the number to print")

loop = int(input("enter the number of steps"))

for i in range(loop,0,-1):
	for j in range(i):
		print(number,end=(""))
	print("")
	

'''
44444
4444
444
44
4

'''

