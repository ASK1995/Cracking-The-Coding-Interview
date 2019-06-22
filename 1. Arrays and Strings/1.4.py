from collections import defaultdict

def is_palindrome_permutation(str1):
	d = defaultdict(lambda : 0)
	odds = 0
	for letter in str1:
		if(letter == " "):
			continue
		lowered_letter = letter.lower()
		d[lowered_letter] += 1
		if(d[lowered_letter] % 2 == 0):
			odds -= 1
		else:
			odds += 1
	if(odds == 1):
		return True
	return False
	
x = is_palindrome_permutation('Tact Coa')
print(x)