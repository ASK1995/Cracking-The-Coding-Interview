def zeroify(x):
	rowz = [False] * len(x)
	colz = [False] * len(x[0])

	for i in range(len(x)):
		for j in range(len(x[i])):
			if(x[i][j] == 0):
				rowz[i] = True
				colz[j] = True

	for i in range(len(x)):
		if(rowz[i]):
			for j in range(len(x[i])):
				x[i][j] = 0

	for i in range(len(x[i])):
		if(colz[i]):
			for j in range(len(x)):
				x[j][i] = 0

x = [ [0,1,2,3,4,5] ,[1,0,4,6,5,8], [5,4,8,3,7,6], [1,2,3,4,5,6], [7,8,9,10,11,0]]
zeroify(x)
		
print(x)