#!/usr/bin/python3

def simple_triangle(num):
	for i in range(1,num):
		for j in range(i):
			print(i,end=(""))
		print("")

number = int(input("enter number"))

simple_triangle(number)




'''
pattern:

1
22
333
4444
55555



'''