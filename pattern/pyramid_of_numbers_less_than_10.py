#!/usr/bin/python3

k=1
n=5
for i in range(1,6,2):
	for h in range(n,1,-1):
		print(" ",end="")
	n=n-2		
	for j in range(i):
		print(k,end=(" "))
		k=k+1
	print("")


'''
    1 
  2 3 4 
5 6 7 8 9 


'''
