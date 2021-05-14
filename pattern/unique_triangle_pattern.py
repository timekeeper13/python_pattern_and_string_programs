#!/usr/bin/python3

number = int(input("enter number of steps"))

h = number*2-1

for i in range(number):
	for m in range(h):
		print(" ",end="")
	h=h-2
	k=i
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
 1 2 3 4 5 6 5 4 3 2 1 


'''
