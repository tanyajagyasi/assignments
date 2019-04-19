# function to get a string made of 4 copies of the last 2 characters of string

def insert(string):
	val=' '
	val=string[-2:]*4
	return val
print("hello")
print(insert("python"))
print(insert("exercise"))
