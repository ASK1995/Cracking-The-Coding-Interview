def urlify(string, length):
	l = len(string)
	res = ['']*(l)
	l -= 1
	for index in range(length - 1, -1, -1):
		if(string[index] == ' '):
			res[l] = "0"
			res[l-1] = "2"
			res[l-2] = "%"
			l -= 3
		else:
			res[l] = string[index]
			l -= 1
	return "".join(res)
	
x = urlify("Mr John Smith    ", 13)  
print(x)