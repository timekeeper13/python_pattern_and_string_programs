#!/usr/bin/python3

number = int(input("enter number of steps"))

for i in range(1,number+1):
	for j in range(i,0,-1):
		print(j,end=(""))
	print("")


'''
1
21
321
4321
54321
'''