t = int(input())
pattern = '*.'
for i in range(t):
	pat_input = input()
	l = int(pat_input.split(' ')[0])
	c = int(pat_input.split(' ')[1])
	for j in range(l):
		for k in range(c):
			if j == 0 or j == (l-1) or k == 0 or k == (c-1):
				print(pattern[0], sep='', end='')
			else:
				print(pattern[1], sep='', end='')
		print()