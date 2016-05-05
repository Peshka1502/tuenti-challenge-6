#!/usr/bin/env python
#
# Tuenti Challenge 6 - Challenge 9
# Taras Sotnikov

import sys

def obtain_next_mult(n, carry):
	for i in range(10):
		if ((n * i) % 10 + carry) % 10 == 1:
			return i

def step(n, carry, count_1, count_0):
	if n % 10 == 0:
		return (n/10, 0, count_1, count_0 + 1) 
	elif n % 5 == 0:
		return (n/5, 0, count_1, count_0 + 1) 
	elif n % 2 == 0:
		return (n/2, 0, count_1, count_0 + 1) 
	else:
		multiplied = n*obtain_next_mult(n%10,carry%10) + carry

		if multiplied != 1:
			new_carry = multiplied / 10
			return (n, new_carry, count_1 + 1, count_0)
		else:
			return (-1, -1, count_1 + 1, count_0)


n_cases = int(sys.stdin.readline())
for i in range(n_cases):
	n = int(sys.stdin.readline().strip())

	carry = count_1 = count_0 = 0

	while carry != -1:
		n, carry, count_1, count_0 = step(n,carry,count_1,count_0)

	print "Case #%d: %d %d" % (i+1, count_1,count_0)





