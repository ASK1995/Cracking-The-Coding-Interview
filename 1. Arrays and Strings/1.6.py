def compressor(string):
	res = ""
	prev = string[0]
	count = 1
	for index in range(1 ,len(string)):
		if(prev == string[index]):
			count += 1
		else:
			res += prev + str(count)
			count = 1
			prev = string[index]
	res += prev + str(count)			
	return res


x = [compressor('aabcccccaaa'), compressor('wwwwaaadexxxxxx')]
print(x)