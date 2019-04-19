#to remove the nth index character from a non-empty set

def remove(string,n):
	a=string[:n]
	b=string[n+1:]
	return a+b
print(remove("python",3))
print(remove("python",0))
