
n = int(input("enter number of alphabets : "))

sample = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for i in range(n+1):
	for s in range(n):
		print(" ",end="")
	n=n-1
	for c in range(i):
		print(f"{sample[i-1]}",end=" ")

	print("")


'''

      A 
     B B 
    C C C 
   D D D D 
  E E E E E 
 F F F F F F 
G G G G G G G 

'''