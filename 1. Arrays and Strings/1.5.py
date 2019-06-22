def oneDifferent(str1,str2):
	index2 = 0
	for index in range(len(str2)):
		if(str1[index2] == str2[index]):
			index2 += 1	
		else:
			if(index2 - index   >= 1):
				return False
			index2 += 1
			if(str1[index2] == str2[index]):
				index2 += 1
			else:
				return False
	return True		
	

def oneEditAway(str1,str2):
	if(len(str1) == len(str2)):
		different = 0
		for value1, value2 in zip(str1,str2):
			if(value1 != value2):
				different += 1
		
		if(different == 0 or different == 1):
			return True
		return False
	else:
		if(len(str1) > len(str2)):
			return oneDifferent(str1, str2)
		else:
			return oneDifferent(str2, str1)
		

x = [oneEditAway('pale', 'ple'), oneEditAway('pale', 'pales' ), oneEditAway('bale', 'pale'), oneEditAway('pale', 'bae')]
print(x) 