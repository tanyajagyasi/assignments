#function that takes the list of words and returns the length of longest one

words=["cpp","java","python"]
	
for i in range(len(words)-1):
	if len(words[i])>len(words[i+1]):
		print "largest=",words[i]
	else:
		print "largest=",words[i+1]



