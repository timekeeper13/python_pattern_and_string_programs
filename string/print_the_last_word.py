
def last(s):

	last = ""

	for i in range((len(s)-1),0,-1):
		if s[i] == " ":
			return last
		else:
			last = s[i]+last

string = "print the last word"
print(last(string))