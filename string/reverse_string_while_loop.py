

def rev(s):
	string_new = ""
	count = len(s)

	while count > 0 :
		string_new = string_new + s[count-1]
				
		count = count-1
	return string_new

s = "reverse a string"
print(rev(s))
