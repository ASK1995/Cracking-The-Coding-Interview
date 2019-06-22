def is_rotation(str1, str2):
	x = str2 + str2
	if(x.find(str1) != -1):
		return True
	return False
	
	
z = is_rotation("waterbottle", "erbottlewat")
print(z)