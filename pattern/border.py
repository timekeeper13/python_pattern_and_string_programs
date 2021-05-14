#!/usr/bin/python3

def straight(size):
 	for i in range(size):
 		print("*"+" ",end="")
 	print("")

def border(size):
	inner_size = size-2
	straight(size)
	for i in range(inner_size):
		print("*"+" "*((inner_size*2)+1)+"*")
	straight(size)

size = int(input("border size"))


border(size)