#!/usr/bin/python3
k=0
for i in range(0,5):
	k=k+i
	for j in range(i):

		print(k,end=(" "))
		k=k-1
	k=k+i
	print("")

'''
1 
3 2 
6 5 4 
10 9 8 7 

'''