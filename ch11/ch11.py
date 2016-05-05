#!/usr/bin/env python
#
# Tuenti Challenge 6 - Challenge 11
# Taras Sotnikov

import sys

n_cases = int(sys.stdin.readline())
for n_case in range(1, n_cases + 1):
	line = sys.stdin.readline().strip().split()
	N = int(line[0])
	M = int(line[1])
	K = int(line[2])

	initial = N * M
	if (K < initial) or (K % M != 0):
		print "Case #%d: IMPOSSIBLE" % n_case
	elif (K == initial):
		print "Case #%d: 0" % n_case
	else:
		normalized = K / M - N + 1
		binary = bin(normalized)[2:]
		count_ones = binary.count('1')
		lenght_bin = len(binary)

		count_steps = lenght_bin - 1 + count_ones - 1
		print "Case #%d: %d" % (n_case, count_steps)