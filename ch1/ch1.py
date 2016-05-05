#!/usr/bin/env python
#
# Tuenti Challenge 6 - Challenge 1
# Taras Sotnikov

import sys

n_cases = int(sys.stdin.readline())
for i in range(n_cases):
	n = int(sys.stdin.readline())
	result = 0
	if 1 <= n <=4:
		result = 1
	elif n > 4:
		result = int(round(n/2.0 - 1))
	print 'Case #%d: %d' % (i + 1, result)