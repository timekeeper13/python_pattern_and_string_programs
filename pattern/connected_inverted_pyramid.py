#!/usr/bin/python3

number = int(input("enter the number"))


for i in range(number):
	for x in range(i*2):
		print(" ",end=(""))

	for j in range(number,0,-1):
		print(j,end=(" "))
	for k in range(1,number+1):
		print(k,end=(" "))
	number =number-1


	print("")

'''
5 4 3 2 1 1 2 3 4 5 
  4 3 2 1 1 2 3 4 
    3 2 1 1 2 3 
      2 1 1 2 
        1 1 

'''