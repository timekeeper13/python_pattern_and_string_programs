
n = int(input("enter number of steps : "))

m = n
for i in range(n+1):
	
	for k in range(m):
		print(" ",end="") 
	m=m-1

	for j in range(i):
		print("*",end=" ")
	print("")


'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

'''
