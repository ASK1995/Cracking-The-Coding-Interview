#with hash

from collections import defaultdict

def is_unique(str):
	d = defaultdict(lambda : 0)
	for i in str:
		if(d[i] > 0):
			return False
		d[i] += 1
	return True
	
# Time Complexity: O(n) Space Complexity: O(n)

#without additional data structures

def is_unique2(str):
	str = sorted(str)
	previous = None
	for current in str:
		if(previous == None):
			previous = currrent
		elif(previous == current):
			return False
	return True

 