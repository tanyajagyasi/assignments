#program to remove the characters at odd index


def name(string):
	new=""
	for n in range(len(string)):
		if n%2==0:
			new=new+string[n]	
	return new

print(name("tanya"))

