from collections import defaultdict

def is_permutation(str1, str2):
	d = defaultdict(lambda : 0)
	for i in str1:
		d[i] += 1
	for i in str2:
		d[i] -= 1
	return all(value == 0 for value in d.values())

x = is_permutation('dog' , 'god')
print(x)