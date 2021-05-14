#!/usr/bin/python3

num = int(input("enter the number"))
x=num*2-1

for i in range(num+1):
	for m in range(x,1,-1):
		print(" ",end=(""))
	print(0,end=(" "))
	for j in range(1,i+1):
		print(j*i,end=(" "))
	x=x-1

	print("")


'''
    0 
   0 1 
  0 2 4 
 0 3 6 9 
'''