
def rev(s):
	string_new = ""
	for i in s:
		string_new = i + string_new
	return string_new

s = "reverse a string"
print(rev(s))
