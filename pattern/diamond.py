#!/usr/bin/python3

n=input("enter")
n=int(n)
x=int(input("add space between two diamonds"))

def diamond(n):

	k=n-1
	for i in range(n):
		for j in range(k):
			print(end=(" "))
			#sprint("*",end=(""))
			
		
		
		for j in range(i+1):
			print("*",end=(" "))

		for j in range(2*k+x):
			print(end=(" "))
		k=k-1
		for j in range(i+1):
			print("*",end=(" "))

		print(" ")

	k=n-1
	for i in range(n):
		for j in range(i):
			print(end=(" "))

		for j in range(k):
			print(" *",end=(""))
		for j in range(2*i+2+x):
			print(end=(" "))

		for j in range(k):
			print(" *",end=(""))

		k=k-1
		print(" ")






diamond(n)
diamond(n)
diamond(n)