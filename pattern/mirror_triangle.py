#!/usr/bin/python3

num = int(input("enter the number"))

x=num*2-1

for i in range(1,num+1):
	for m in range(x,0,-1):
		print(" ",end=(""))
	x=x-2

	for j in range(1,i+1):
		print(j,end=(" "))
	print("")


'''
         1 
       1 2 
     1 2 3 
   1 2 3 4 
 1 2 3 4 5 

'''