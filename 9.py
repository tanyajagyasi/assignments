#function which reverses a string if it's value is multiple of 4

def reverse(string):
	name=' '
	if len(string)%4==0:
		print(string[::-1])
	else:
		print(string[::])
	return name

print(reverse("tanya"))
print(reverse("ritu"))
