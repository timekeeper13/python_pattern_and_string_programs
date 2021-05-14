#!/usr/bin/python3

number = int(input("enter number of steps"))
h=number*2-1
for i in range(number):
	k=i
	
	for h in range(1,h+1):
		print(" ",end=(""))

	h=h-2	
	
	for j in range((i*2)+1):
		
		if j<=i:
			print(j+1,end=(" "))
		else:

			print(k,end=(" "))
			k=k-1


	print("")


'''
         1 
       1 2 1 
     1 2 3 2 1 
   1 2 3 4 3 2 1 
 1 2 3 4 5 4 3 2 1 

'''