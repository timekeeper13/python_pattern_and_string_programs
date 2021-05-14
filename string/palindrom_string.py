
def palindrom(s):
	s = s[::-1]
	return s

s = "lool"

if palindrom(s) == s:
	print("string is palindrom")
else:
	print("string is not palindrom")